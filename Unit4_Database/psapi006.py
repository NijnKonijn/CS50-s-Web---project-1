import requests
import requests.auth
import json

BaseAddress = "https://psapi006.unit4saas.com/U4WebApi/"
ClientID = "U4PS-DEVOPS-PAYcheck"
ClientSecret = "067617d5-a93f-403b-984f-18e919252655"
Scope = "u4ps-webapi-tst"
TokenAddress = "https://ids.tst.unit4online.com/identity/connect/token"
AccessToken = " eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Img3cTgyZlV2MEgtdXBKcDAwV0U4cXpyMUh6RSIsImtpZCI6Img3cTgyZlV2MEgtdXBKcDAwV0U4cXpyMUh6RSJ9.eyJpc3MiOiJodHRwczovL2lkcy50c3QudW5pdDRvbmxpbmUuY29tL2lkZW50aXR5IiwiYXVkIjoiaHR0cHM6Ly9pZHMudHN0LnVuaXQ0b25saW5lLmNvbS9pZGVudGl0eS9yZXNvdXJjZXMiLCJleHAiOjE1NTkzMTc2MDEsIm5iZiI6MTU1OTMxNDAwMSwiY2xpZW50X2lkIjoiVTRQUy1ERVZPUFMtUEFZY2hlY2siLCJ1bml0NF9pZCI6IjZDRDc0OUZBLURDOUQtNDU2NC05NUJDLUY1MzZFQzM4RkQ2RCIsInVuaXQ0X3NhbGFyaXNfY2xpZW50X2Ric2VydmVyIjoiV0VBWi1QUy1BUEkwMDZcXFNRTDIwMTYiLCJ1bml0NF9zYWxhcmlzX2NsaWVudF9kYiI6IkRldm9wcyIsInNjb3BlIjoidTRwcy13ZWJhcGktdHN0In0.mQnQ02XklyLO17tiWuc-QuPh0J-5ZYPkG1jEcWRW8-rr7OBKwnb6ExI6U_fMZU0PPKWJbo9y4uvtRIJ2oXaz1kWSQnvwXrq3l0WxYasFORZnbRJiVAw43JUfY9VXWjP8YOA2eS32DcDLLUnbC7srVrRvd5aO-ER5f75qyxOhLDG2JH2UigUzT-Tu3dQlDiuS8DAo1E55bD9GZ0TYvbZT6YeM-TpIKP97c-HApiAjBc1DuuIt_4Jlq9Xux0zCDzQbuxSVL6ecjHKuu9v2KE2QEDwbmNm1hgjVUUcHWkLYQIxXLlOVSlS4zMCqpPoDo-NAQKrjbBAxHheqt4SHJnYjlg"
Database= "Devops"
GrantType = "Client Credentia"

data = {
    "BaseAddress": BaseAddress,
    "ClientID": ClientID,
    "ClientSecret": ClientSecret,
    "Scope": Scope,
    "TokenAddress": TokenAddress,
    "AccessToken": AccessToken,
    "Database": Database

}

r = requests.get(url = BaseAddress, data = data)

BaseAddress = "https://psapi006.unit4saas.com/U4WebApi/api/v1/employers/100200/employees"
req_u4 = requests.get(url = BaseAddress, data = data)


