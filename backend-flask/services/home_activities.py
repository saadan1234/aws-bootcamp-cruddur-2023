from datetime import datetime, timedelta, timezone
from lib.db import pool, query_wrap_object, query_wrap_array

class HomeActivities:
    def run(cognito_user_id=None):
        # print("HOME ACTIVITY")
        #logger.info("HomeActivities")
        # with tracer.start_as_current_span("home-activites-mock-data"):
        #     span = trace.get_current_span()
        #     now = datetime.now(timezone.utc).astimezone()
        #     span.set_attribute("app.now", now.isoformat())

            sql = query_wrap_array("""
            SELECT * FROM activities
            """)
            print(sql)
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    # this will return a tuple
                    # the first field being the data
                    json = cur.fetchone()
            return json[0]
