from typing import Any


class UserProfile:
    def __init__(self, user_id: str, raw_data: dict[str, Any]) -> None:
        self.user_id: str = user_id
        self._raw_data: dict[str, Any] = raw_data
        self._preferences: dict[str, bool] = {}
        self._activity_log: list[str] = []

        if "user_prefs" in self._raw_data and isinstance(self._raw_data["user_prefs"], dict):
            self._preferences = {k: bool(v) for k, v in self._raw_data["user_prefs"].items()}

    def get_username(self) -> str | None:
        if "details" in self._raw_data and "name" in self._raw_data["details"]:
            return str(self._raw_data["details"]["name"])
        return None

    def log_activity(self, activity: str) -> None:
        self._activity_log.append(activity)


class ReportGenerator:
    def generate_user_activity_report(self, profile: UserProfile) -> str:
        report_lines: list[str] = []
        username: str | None = profile.get_username()
        report_lines.append(f"Activity Report for User: {username if username else 'Unknown'}")
        report_lines.append(f"User ID: {profile.user_id}")  # Accessing public attribute

        report_lines.append("\nPreferences:")
        # Tightly coupled: Accesses UserProfile's '_preferences' directly.
        # If UserProfile changes how it stores _preferences, this breaks.
        if profile._preferences:
            for key, value in profile._preferences.items():
                report_lines.append(f"  - {key}: {'Enabled' if value else 'Disabled'}")
        else:
            report_lines.append("  No preferences set.")

        report_lines.append("\nActivity Log:")
        # Tightly coupled: Accesses UserProfile's '_activity_log' directly.
        # If UserProfile changes how it stores _activity_log, this breaks.
        if profile._activity_log:
            for entry in profile._activity_log:
                report_lines.append(f"  - {entry}")  # noqa: PERF401
        else:
            report_lines.append("  No activity logged.")

        return "\n".join(report_lines)


class SystemFacade:
    def __init__(self) -> None:
        self._user_profiles: dict[str, UserProfile] = {}
        self._report_generator: ReportGenerator = ReportGenerator()

    def add_user_from_raw_data(self, user_id: str, data: dict[str, Any]) -> None:
        profile: UserProfile = UserProfile(user_id, data)
        self._user_profiles[user_id] = profile
        print(f"User {profile.get_username()} added.")

    def record_user_login(self, user_id: str) -> None:
        if user_id in self._user_profiles:
            # This uses a public method, which is better, but ReportGenerator
            # still directly accesses _activity_log.
            self._user_profiles[user_id].log_activity("User logged in.")
        else:
            print(f"Error: User {user_id} not found.")

    def get_user_activity_report(self, user_id: str) -> str | None:
        if user_id in self._user_profiles:
            # SystemFacade knows ReportGenerator needs a UserProfile instance
            # and ReportGenerator knows internal details of UserProfile.
            profile: UserProfile = self._user_profiles[user_id]
            return self._report_generator.generate_user_activity_report(profile)
        print(f"Error: User {user_id} not found for report.")
        return None
