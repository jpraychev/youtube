from google.adk.agents.llm_agent import Agent

from datetime import datetime
import pytz

def get_current_time_in_city_pytz(city: str):
    """
    Returns the current time in a specified city's timezone using pytz.
    
    Args:
        city_timezone_name (str): The IANA timezone name (e.g., 'Europe/London').
    Returns:
        str: A formatted string of the current time in that timezone.
    """

    cities_timezones_pytz = {
        "London": "Europe/London",
        "Sofia": "Europe/Sofia",
        "New York": "America/New_York",
        "Tokyo": "Asia/Tokyo",
        "Rio de Janeiro": "America/Sao_Paulo",
        "Moscow": "Europe/Moscow",
    }

    zone = cities_timezones_pytz.get(city)
    if not zone:
        return f"Error: City '{city}' not found in timezone mapping."
    try:
        tz = pytz.timezone(zone)
        now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
        now_in_tz = now_utc.astimezone(tz)

        return now_in_tz.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown city '{city}'"
    except Exception as e:
        return f"Error getting time for {city}: {e}"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_current_time_in_city_pytz]
)
