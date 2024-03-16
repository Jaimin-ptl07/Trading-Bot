from fyers_apiv3 import fyersModel
import webbrowser

redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
client_id = "RJC7C5X-100KJ5"
secret_key = "Q3HPEDFV3U"
grant_type = "authorization_code"
response_type = "code"
state = "sample"

appSession = fyersModel.SessionModel(client_id=client_id, redirect_uri=redirect_uri, response_type=response_type,
                                     state=state, secret_key=secret_key, grant_type=grant_type)

def generate_auth_code_url():
    generate_auth_code_url = appSession.generate_authcode()
    print(generate_auth_code_url)
    webbrowser.open(generate_auth_code_url, new=1)


# connect to broker
def connect_to_broker():
    access_token = ""
    auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MDY4NjQwMDksImV4cCI6MTcwNjg5NDAwOSwibmJmIjoxNzA2ODYzNDA5LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYSjA2MjMzIiwib21zIjoiSzEiLCJoc21fa2V5IjoiODVlMDE4ODQ0M2VkYzNiMmMwYTI0MjY1M2ZiMTlhMjBkZTlhZjI4ZGE3NTBjYjMzNzRjNThlNmYiLCJub25jZSI6IiIsImFwcF9pZCI6IlJKQ0tKNTdDNVgiLCJ1dWlkIjoiNWEwNjUyMWQ0NTRmNDQ4MDkyMTA0NzQyY2E1MzA3N2MiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.bFKih94CjY2etT8uvRmWA-4moLOL2IiRYI3oM22yzd4"
    appSession.set_token(auth_code)
    response = appSession.generate_token()

    try:
        access_token = response["access_token"]
    except Exception as e:
        print(e,
              response)

    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="fyers_log/")
    print(fyers.get_profile())
    print(fyers.funds())


if __name__ == "__main__":
    #generate_auth_code_url()
    connect_to_broker()
