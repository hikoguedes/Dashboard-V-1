import os
import csv
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import io  # Para manipulação de dados em formato de bytes
import numpy as np
# from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# import plotly.express as px
# import plotly.graph_objects as go
# import plotly.io as pio
import locale
import altair as alt
import matplotlib.ticker as mticker
import pygsheets
import plotly.express as px
import bar_chart_race as bcr
import datetime
import matplotlib.pyplot as plt
#import ace_tools as tools
#from sklearn.linear_model import LinearRegression


plt.rcParams['animation.writer'] = 'pillow'



# Configuração do layout
st.set_page_config(layout="wide")
# Lendo o arquivo XLSX

#credenciais = pygsheets.authorize(service_file="Kempisnki-chave.json") 
#ArquivoKempinskiGoogleSheets = 



# URL compartilhada do OneDrive/SharePoint
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA1MjkyMzMifQ.PiGt_QWGY8WlbaJsYlr439vokYU_QJLC6PrKZ6bm8vJ3INjtofuwUce6FYwicUkmX4NV1zY6IVU2y_iyHUJKBzCI5KEGsjRerLOO6-0C0IDhS3b36YPRWLqeL9JWqyfSNefMfj5m5pWZ0ZXP3tt7ARdZzeTuFiRxUWKCDDytelbLcyF2kxURBnZTdyGd8mZYITI-EcBYn8c57OH4QZIZhtJ0UZNvYSZ47Ejqndiu6XGrR-9x67PLcPKZJGiCQcwmGSvQt_6hZvP8xLAlEeS6G3M_e7a7pQ0nahX_YgCl4s0Rv7o3Wt3RlUcaJESJh45bC_OEoVb319VoFXKFP079dsnZkhKhL9cd42mlvpY2N9KMoyhDeev6I2afX4mf7r8P-N9Yd68dbYqJGtphRVkw8w.lCXl9JPJrmetVmAR8BsrlEZSHrQNPLLeCeBYpI-XaW4&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA1NzczMTcifQ.I4JXk2odmnYrajfe31XhbahQG1o_W-A8wVDL_y1BYpE6aksinQqRT2chhuH1SsqqXBvOe9nuFfaNjZfOesMzKbIy8xPkMK771Jl3cEt3-8Q7dt4UmBX1IOa2z6VEyPszPHz9tgkGD4spVldbrll31_OIs4v1_ubMQ1Kdg0ZNhOAIIjiHPn4V0ef_3z2JoF4pg58rK6thfkPIXjqOWH2_OuqWAU_kfLXPFhCsgnxbQkpApmHIQ8R3ygPCHcK3YbFR99yGqINcZ6KGvGcQAOGXggEewHP--TXE3-LWOcth2M7PS8BPxUcsjW98syhrZuczRy91_Q7rbqQCcse315vfM87TsrmHCbEuxuSiNn7pFEzIdu7xHhlODn3XGZMk7YkczgC7kd_tQMPmyvaInRNEfQ.aZBPjVRLEUyw_RsZ77QA9cOwU5klY-rDI4ttsZpBQNY&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA2NjcwMzMifQ.BrSeSfodAOPMkAvhGM0hkYp3ESRbsBQ_jasYnUD1lHR0rwM0D85GEj-7oSckcpWo_xiYVV4FLDwEVTPvJXKEiqV-0kmhCwPYvStuKbi02Id5DSKrG5-81fKeIrDURfbhha3FPyDs3GWeK9cw06jmzzuF8AKWcnfB057G3kN3CmIRi8M79qGdrD6nSKHnx_HCAsAk-X7mtPbVk8pBLsowSob9S-pPNr6i5r-la3qm9lcPDzvCCRrk5tnscF-IbwaayP9nvoC-m-94OCS7DET3NeYLXAhGNP0AV7iZgSu_VWSX1oefRPLN2WQDNGZqmhKESwJVGj8wG_soQvOj3evvzTnXKL0nucEFzjhIam74_AY096_iGkw9xrW5NRhXJlxW6mGQ4RfDuJc426jMOzbffg.AUpanadYuIfXfK6unC6VojJM3FNc3gtuxr2h7ikqHFA&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA2NzA5NjQifQ.NY2FM6GVClZzVNYtNkZF9zlkPnEZRkiaWnmqkBhBRbmDsMzUlziYOrNCKf6IvfVYMg4Hlfv-I8eUqs-UnBCrthm0CCx3u_gXU7jC14PiOPbgyGisKvFaWPZpOegPCQhSQK700L4aJFXMF70WlzvmT51o1BPBXG_gphuvXqqbxGpZMSdF-bKhmVf7OjW8DucsthHA_Nir9qXUWt8g-Shz8nIPid6ZIe106Jn1t2DlHV6FZ9IK1FBvgeyP3xXccwF-HzKB55eucxSUZhQCXdegqbAsyLz-Swvb2J10SyYcqyZ9P9QsdelBIpiXSWTCIgxFe5IYYhZNnbPKuhhCZ9WLT5GZe5nXCx_IUim1FkvpxSbJbAR2Qjl7qClLDDhPJAnmqyibHNiebTRL0ecp0W5CWA.DzLWVVgVVjHxZLA09Bsgfq09nN8OMe2YqClJ7atgbfg&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA2NzY3NTMifQ.hgKzGcFLQgWjn2JItcDOSvHT0Jq8gQ1zi10finxxWifnslaWKjDVGteQJTtvx_b0ifaoiPhVSQKnBryIirVRsTnUpNqxF3cBIUr1umXC1gvaJO3LEJ_nvX6k0qj-iiYqFMleCL8VTrV2b_nch20HuMoaoOOj4cnt_Ug3b4hONSynZQo0CfpF_Sk7qnuZAIVrzwQXBaMeO41uXopsuBTN42eyTF2wQF6vZBuh0Hl_bRfju9vgRdPXdNY2eJajG2YcpFpOA9x4CfqeiDQgHZRxHz5jCiAPpSHXPqyFhHfKh6eHCrzqU1TiiCZRKM54R5sOUeNE0f6siYG3Wn08DB9XdoepvVwhrJNVxCk69aSJADt3qD1WLOJWn1yxlOVY6Pps3j72LAglrXDKPOOLQ7l-oQ.OYmKYI7iW9BeyVvhESF_qFaIJIgSivqsl1ueg0M0umk&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA2ODA4MzgifQ.5nbvZR-D6ErPSe0A4t2S1GxO4mzI4tKJjrPDFKDSRAXH6C4VHaeXcRUHQcM--KgNOJSKkGT10PIz7TTR_x_R4pBa6LQtT8qMyhgpJTN5C9NLJ9CCw6ZWEYuYSrEN_Yq8AmeaWy1jaTLPRWZVwHvWCRZFkniOv_lePHy_6UbhvgQJSI2AhigtTjiVmVXLAt0RsJrGbyfl51Bmbnt3KQjHNbpaGjG_LZh1Wxxg-kSTtxlNxWOmoVC6J-uAYRCd0rpEAdxy7qU3qtClpr6FeHHlFnpCgPUAylFx4kRqmtZj0kVT2E9vIwmm8gwtxqdpkLS-dHHW04XLJldgg8Z9UGDFi6Sb25Cq8RPPRwgNXtJzZ1K4sEPFHHtCM4TJo6JSzrvvCvwlw5qNvvle8_Ps2_dasQ.cVa5e15odm5yQM9AJr-hY7NRECb4cOWkd9PgYf3CSlI&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA2OTEwNjgifQ.hBs5AXy7uBRxrcHDuk19iDFKiWhcPS-5W3f-XtMDFGtTt03Dur6sbDFzu4qFHlyvO84PYQRZzapNxqHxWOw5GeFKlESbmgRgYKmlCZ6EevOYNjZjFhuvw7KV3Ja2pFDxiPAxtJB4aW-DEorF8qEL5Z0DnomnAXbCeZvrh66LsQqD__EsuqDqdlKF2YZAcrENzHaccAQq_9w6Xe5aak2PA3oLZSmRuRDJlTl0mLOmBKRGLJ7eKNyEteFOUiNZvwawcW68YZLlmoAsp4KjRMdnUaQeiCgsEY8UJdYOGI3syCzJxF7spBKPdfM_dkUum7avaY8UFidM0f_1Y5CVNozsWGD8J46u4vKR6CefF4HnwCkKFw4M0pclg8LL13JXTzC2m1TIYTXNp2xanXg5wA06Lg.IDnsKLyNAh7V-haXlX1SiOIohwH5lUtG15FC4f9R5XE&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3MDY0MzAifQ.NcbfTTMxcr6k0LqSdNz0IAjSgEUybh37SS14OxzU5RMvflBT8z2ZasThTQTg5q6f-PxS76h4qK3RZVfBsQMzUwlbZ_IRKxtc20P1Nzjeg-pauP5wM0lALWviF1Rsj4xUNGwMmvRcYviUGIc-4UQCNlFDR7Ppw9PpT91VVzpk4Qx_9UB3T6yJREIEXc_Kj2Z7MVR_43WFzJMY23ppXKpAP8QLYsq2q1q9mGe8GTcfGdvwwrqxU-_V5WqQe53Mk3wW2W4z1WXbogu3giV5DS8RPD0JNhlZIbK0YnVoMFt8S9QnAQQKGg9i7wnYg1vG-UOqkEgozgMxb62o2Wr0x5jLqNDUqxhtQnJi_Ovn3cNVWwwQ7e3TRX8a9xhDFaIW_oiyo8leCVwZyWWcXrqK2wR7ag.I0CSMPQ06K3zcm_3KXVsgC4yTeWGVWQEO4de3As9p6U&ApiVersion=2.0"

#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3MTAzNTAifQ.rVZMvdaIFT0Jin1dANxtbBvcl8MhmYwcRcsLP9iU0sq6klAiPsA0kkGdFdgejzvM-i5DZE2VZWiZN0HAEUEUdT3CyZb43PN_Lyl0It3R9Ai-5Ac9dJh9b34euuCw8jz4NzOT7R93t18oshsSn_NcwFYMlzzt0S-73ZarD2LuT72LfJ-GMYFfJUwbI7x-eXgR3Ffsfx064DyV9651ObAZmgmBxy6axCkMa_vT9VUQGsqGFS1XxF4U5U1kTXRePWDkbZrx4TeHTyqznf5Hd6vi3Fsh0rg6USxMRGvFnUeLkzg4VOqLJEa9QclXPATYUmpp13XTcoMJcMPBJTEJowYEeQifXIQpPbF_mN22UFVlK9kVt4PS4bxXtshqH0iFp3QRRBIQscArW1PX07ILXPFtYQ.MU0YshN-5oieXGjWsjS8PFBS3mfMu9FNXcOU-lRcXlA&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3NDk3NjgifQ.K3-_b5qbxl7JbzRlo1a-G4ybBxWVgvFvHxgbJkYjvNQYsy6yIBr0ZNyp7w_0yvCzkKX0F7qqlKjMXTKIk_aSCUM8b54a5lQ4mgwIZkpecuqn5bCYVQ_my0HjCdgnmYsoQreQZALmWRQ6niU4_NG8R-hBgHujPByv7DU7Qdrn3_zRUxyor-l82PiK_7At4XCtLgXi-lLOqZTy-hTS8d1PW0yfrwlYaHFpUA5G5cpOnbH-cxPr0cedB46jcPC7-WqbhCEottFNczl_OC9A2O_qUTP1oJ64KtcgJbTmwe-cxG42SeVDEYFvBC3TYcN9ec2nh5S2dEVTuqlj9zZj7OyYAEiJEi3SkQRm0zrM45NOrFjwGgisYzwFXQk9xFJB019-Fyf_7a21bIlaCT070lwNiQ.wmMihxUFfvZRwhwlfFsu3O7fB-X_hXlwYr7BMVl7NuI&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3NTgxMzIifQ.nY1S4SySCUJwdiK9C3y17uBiBbGCBkM7YfCc8Dbx4mrQDKJxw4BaMlBltmUfKv3R3nwGDvPqgh5Z5vQD4phL2JYsZPnf4BM1Puc7bsi6GCs8e6hiYf4Bsnr1tgQmj3F2j9M9J_lN7xa2xIZKS7658Qb6VoXtErUP1zOxzUZyyPENsBL_9Uc3iPySsMLQ1RwI_Y7vafSoBvXS4VmQkJXvRZzUqO9khDyrooBdBzrz2O5sQfZdRdlWXM32hrWdS8Qosd9PSPFKjPJT6QM-eC490B4hz0jXZOjS1n6Yu8h3-rSzoU-434PPvDKsxIz-1x2zI6YmnP4nEFUjeHWuDKuuA-wkKrIHJmdBHW8mIFT0QNrbGEspjThVS43tH1APuNoOHxzG2irIU7QbD19tw2G-Eg.nhHdc68y_G74wzMx_PyiMlM8v__5q92xXFRmoRLvhyE&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3NjQ1ODkifQ.z6TtNHZ4NR2PMaaxFbVu9MhWyRmlu5U5Uf6Xd_18TqtDldnm-S2Wr2xJogA4mdsqQ2Wge4pjOstlnv1vd_F1ukXLe8-zfHZ4HiGpBiybIqbdqiY1ZDCeSdQiMIGHJaSUzk1teXVoiH-LkTKGCPhga1NDY8jv7liZIKZ2P3Y75gTnlnm2WLRFOzV6wG6HAeQmq3f-xKp8c2-EpRaiFq8exQfdvor-ooiQZtumPLlM3R2pUy_FhQxDhHxIVz1Hlf-_c7vAVbXiGQf-f8a6z3KbeMx0x5cHPB38Yh_UT2EN01ZZ2U9lwWg5-BQYcGJrt9UFRzOiKAG45FUeDovfXghG7Zbl4mi4e9NPGmlPmbc2QeqDlBYT8_xPu-cUhQ9V2LgGyZvNCFUdugecituLNpqaew.nyzZ71Rx2THik_0BTFBmCRBHVcZ6_UGVx13aciXjx4c&ApiVersion=2.0"
#url ="https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3NjkzMjUifQ.uhL8lQUw0X_5SQ8MB6vSg9GgUFgUUNHanVwf8QHG5FHmaiaXS6z-vMRYvot4LkT5QU6y2pIXJa7HwHQ5xulIqQZu8lo0SM7s0NMelw0zII7A5kXolqfNwC1cpSlNiUmvF5B6Us-gdXL2jotShrzhRD78MzuBGS5QXQFX8onVl3WpangSM6qEPmjfY20Oq-RKtpmdOfor8fLD6TssV_lp7JOF89ILjI9k6QqWBPVoPLoRNiRq8E7Yd7RshwIZrWXsGYFyj4uPyz27jrvTEjLZ1eaohYmuLNeB1UcmVYXirRqHLJ0SwGG1RW8kQwHRg_y0RNp_fWvLVCIl2wm7Gp2g4JzonBKxqXObUpnnSx2jmozbCsb21u7_mP8rhYzbC8CoQgze3QdLR8MS-dC4uMELmQ.GB7exDPeNV-MBJvXIYPnFg2mwNgqDHAIysK8Qi0_zm0&ApiVersion=2.0"
#url ="https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3NzM1OTcifQ.xq4a-IImhYHOryXwbqwNhP140nsAzcsAIzbZtGSfC0pb10SVx3lvqfifChwkd6Rh57TmDM5HSf9KmviU1YeX7BFX1LNmyeVtUg1N1D1JwY0jGjDsWGzEaQ6ZAETGSXqXXUKrkJlf9rjhkDdGGHq9VTLdgGoKJjrYJscU5MERz0v0e8jcxCJbt7WRq44ZeGx831dw4mv8CYUknX_9k1Whi6GMdEuV8HU21vCXs7lFMz8EodXs7RX66cnjLccke80rkskK38InVFbnFdA58Ss7IPI5Es23dY74aItp9aN2U7i0PLGrdfMUE_AQRvURXIquLYgGtQP3nY47jSCyrd9vYi5UIbpUsX8sVB0KVRf_vCSfHrPSsVPPR5diLZ3bnXddQypVgLyVlyxx-sZd8ksVcg.XxmF0Bud4yX8o2D-bpcK0rDy60xBHKfZl5pqGrW4kLU&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA3Nzc1NjQifQ.giftI-fV-biLd1wdhQ-g6o146G8LS0aEyRmPafi8xeIGUMah_R4trau3V9nPs5hmO8UQ4Hs0eqLUpCcHUeBHCCgvPd5JaF4K45ZAUSS2R5VXwDSqgK8UNE1Vb_CLyoVFWPwT_LHmD4KhaC10nzbp75RNpms1_ey5PBp8ufUO5CJt-EBMTzWJ9Fbcewq3DOTeRym2TIhiQkQTyoVyDhjPtuP59HOojM1ysBR46fVAor-998nXNMIfWO7ynVbcJaNq06h2bDWo08gJRr3gt-yVOSbMUIzYbhfdT4ciCYAbt1PNURbZcC9lEBW53HoHnD0ES71qRqxzgvr36nGBHvaZ3ENqj1rrvbDvj1PEGOJANe8PgG0MwcFCISaDVD9x_XUFRgEFeZnLmIwe7_dS1C7Jvw.JennxVkHTQzx-eiCacR90Z9KRPas-sSmVNsTMZp7eY0&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDEwMDg3OTQifQ.nPKr5PBMHLFPfWnWEy8JhjvR1kiVaoKGrGv1Clfha_8CL4m9VFIVtjOxQXfdNPfU1nG32FI3np6bKRbFicw2vB3sKSR5-OWcwN-Lt5NYoW-CUzzac-CUBC9_8ofdO1MS0kqB5E08P5MEDadm2DugQwN83B02t3wCSNMcfY6_xbnc058IQpszq0sP7n7XCkygaeVjrwFQpBf1hV-nMNGU44GfB7sxvDISsTG-qh9TijSYCthk7L4ph22Qo_AuWNT93EuFSW3Pw5R_wpZEcvZMPg-0eHM8rNaL2dswNqkYsBrf0Gp5NvDyrocVMYaUhwJbAeNG__25EUgRZY9WLq5wopzF6li1szQmiOQg5VWapC4aLFFiQAUjwY_EqafiQ9Avwpj-IwTc4KRVpbRjTbC1hg.T0nx7HDL4edGcyHiH4hdw0aeC3k7zgQQF6dw-phb6kA&ApiVersion=2.0"
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDEwMTMwOTEifQ.TIBPGj9D1qCRpuGN-CWIkl7JdEX7SvMKSlhlBngSgIuabxNszNKG1GEO9MjbcIJBx67H9buk9_7eR5uQYylbQwe6aNxnwQy00rPqyYE2cvYPyteeDsvbys8yGULts94GcQoqR3-2BfL3Vlgg2churwEhSxwiDHhFHgY65dS7Y-1kbYjYvIU8gqiO75J1or0x66FsB7kb_cgpRGfBhLhys3vgo9G9bXV8K_RHT6WJWpKsxd4xGhyOFJTuU4FIV7lQ5fgFVfkcNVJ7rLz3bbE4Fg6n23sIuDbkAZzeCtGtPsVoJI2N14w7R15IQ8wsP18Ol-upwmnVZBKBQnrSEzqsSDnKV26UCc5BgUEWNY2QLJG5LwRcFK2t4ZqXZ3vAcpqD8CQCeD096MLhkewTwqQcDw.08PGB9YQTD3N5-QUkGVuSEWTbh4TQ4lFN5_m-NFNT8A&ApiVersion=2.0"

#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDEwMTcwNDQifQ.Q_YH_QNX5AJp0Xlb9A6dxAORbYmscSNNeewTJOSmuJ3beNIImTlCJP9idYIHorF-nhfBgGut78Jppz6bODg26T2SKU9NOTj43B5an0hlJFhigsX1xNPIXSbd3-hXZLxLpIu3Sp2iTD_QKAm0AW6ltpTAYuulbUGBvdVNbkzQsfzt1YAiP9mIMeztrZYPIwNtVwYuAcI2F_XWc0Oj0GMQuiKNow3rj2MmgyZINDTqeaO7Eat8VmVJmYK0slC1XGeAYfuf8NN4p4JuLTK9RG96NcktEKSt736CGnbRMFk1JF_zLArOtMt3bhEFIYFmRFUJMpGWm8KJ5Wd-3pAIMTkEDDr0gM2sqnZImzmhxtm9QvNJcYET7_aqWdxiU6aN2a0ynXeYJOdn-7yVEQeb7XC0ng.AUW9l2NwlrWKEN1OdeW2-VU_E6VMia6o7DngA3zeH8s&ApiVersion=2.0"

#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDEwMjM0MjUifQ.3LNABcTPLXT9q3GiRoXizRWzndxrDN9sKH-kPeLufJZ4rsVoeNI9w_i2gPo04_rr-qbi8mFTEEHDcvYHjotULJqYIgNYqy0S5I3Agvt-HmJwyFp6tyY1hzF4ArKe25aHJSNAxLZPsfYWenkE-EhZDf3lcvrJmZvZ8f-Br89ORM2kUmm0cusZ2SwYtXOvhit7E9kSJjn_zfAS60MSLrVF40FXKkpG0jivaP-xxLb3CdFx7MSD0DRrE3pVHSSHNv78VcRD37GDGqkCnxKOpZpNs9AEMpHzS7JH3MWgOq5HDNouGsXU-SdG1lozpT6ccpA5hvRFeXGW7NP0BqOMNZN19bGLoBnlKBH5pHiOAVHDuwi9PcZg2NG_h0a1Iyehk86niNEypqhdS9wzv-UomkEBeg.Ww7nWZIO5LKkK6g04kkPcCYHghDK94qchFIKp4YGp0M&ApiVersion=2.0"
##url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDEwMzU5ODgifQ.-5pkOH1mWhVetkQviHrssEQBx0aoIBPwmKGYB1s3JKyF5heiBzhen8K6OrFa8WP0Rd5xHbnR33OBeOmjPSkMr4tjz0yMhIHih5cOEnRptKcK_yI9xQTO7Uy9mUWqAR5cFfRvppcjAPSiSw5YtOh30FUa-AsCgVSBvmdb6ArXH0Z39rOEaft4pOVyl9KnfWy-9-iFP9MYtYZUt4-GEhzIiRQ4f2p0KItok2nxo7ZF-p4p_AknPaWI3FO_tWGh8K5i2sDaykRyh9BxmyAsKMVTPa-tl1gCtDdkrr9CytnyQE62_KkgVwYhR_za34fUb5HZnTefBeTiLK1dWjl215KxoTO1_I77Ml_e7KVE9KTzcsbe48m7cjTacd-z1_Dm1b3VYhNo7MpaiPj1AxrSD8HUTg.JRCnd2jJD0slrr3vjhgscGmWxuGh2Gav2lC4xfS_K8s&ApiVersion=2.0"


# Função para carregar o arquivo Excel
#try:
    # Nome da aba sem espaços extras
 #   df = pd.read_excel(url, sheet_name="Consulta Contratos", engine="openpyxl")
    #df = pd.read_excel('BASEOFICIAL.xlsx')
  #  st.write("✅ Dados da Planilha:")
    #st.dataframe(df)
#except Exception as e:
   # st.error(f"🚫 Erro ao carregar o arquivo: {e}")

# ============================
# 🔹 FUNÇÃO PARA CARREGAR DADOS (CSV ou XLSX)
# ============================


if "df" not in st.session_state: 

    def load_data(filepath, sep=',', sheet_name='Consulta Contratos'):
        """
        Função para carregar arquivos CSV ou XLSX com tratamento de erros e garantir que a planilha correta seja carregada.
        """
        try:
            # Verifica a extensão do arquivo
            file_extension = os.path.splitext(filepath)[1].lower()

            if file_extension == '.csv':
                # ✅ Lê o arquivo CSV
                try:
                    df = pd.read_csv(filepath, encoding='ISO-8859-1', sep=sep, 
                                    quoting=csv.QUOTE_NONE, on_bad_lines='skip')
                    st.success("✅ Arquivo CSV lido com sucesso usando ISO-8859-1")
                except UnicodeDecodeError:
                    st.warning("⚠️ Erro com ISO-8859-1. Tentando com 'latin1'...")
                    df = pd.read_csv(filepath, encoding='latin1', sep=sep, 
                                    quoting=csv.QUOTE_NONE, on_bad_lines='skip')
                    st.success("✅ Arquivo CSV lido com sucesso usando latin1")

            elif file_extension in ['.xlsx', '.xls']:
                # ✅ Lê arquivo Excel e carrega a planilha correta
                df = pd.read_excel(filepath, sheet_name=sheet_name, engine='openpyxl' if file_extension == '.xlsx' else 'xlrd')
                st.success(f"✅ Planilha '{sheet_name}' lida com sucesso")

            else:
                st.error("🚫 Formato de arquivo não suportado. Use .csv, .xlsx ou .xls")
                return pd.DataFrame()

            return df

        except pd.errors.ParserError as e:
            st.error(f"🚫 Erro ao ler o CSV: {e}")
            return pd.DataFrame()

        except ValueError as e:
            st.error(f"🚫 Erro ao carregar a planilha '{sheet_name}': {e}")
            return pd.DataFrame()

        except Exception as e:
            st.error(f"🚫 Erro inesperado: {e}")
            return pd.DataFrame()

    # ============================
    # 🔹 EXECUÇÃO
    # ============================

    # ✅ Caminho do arquivo
    caminho_arquivo = "BASEOFICIAL0703.xlsx"  # Altere se necessário

    # ✅ Carregar a planilha específica
    df = load_data(caminho_arquivo)

    # Exibir as 5 primeiras linhas no Streamlit
    #if not df.empty:
        #st.write(df.head())


st.session_state["data"] = df

################################CONEXÂO################



# Initialize all variables with default values
def initialize_variables():
    return {
        # Sales and Status Variables
        'VGV_BRUTO': 0,
        'total_desconto_financeiro_sem_cancelado': 0,
        'valor_final': 0,
        'quant_assinado': 0,
        'quant_nao_assinado': 0,
        'df_vendas_agrupadas':0,
        
        # Purchase Latency Variables
        'media_latencia_compra': 0,
        'media_latencia_compra_arredondada': 0,
        
        # Table Type Quantities and Percentages
        'quant_a_vista': 0,
        'percent_a_vista': 0,
        'quant_curta': 0,
        'percent_curta': 0,
        'quant_longa': 0,
        'percent_longa': 0,
        'quant_longuissima': 0,
        'percent_longuissima': 0,
        
        # Monthly Analysis Variables
        'ultima_variacao': '➡️',
        'ultimo_valor': 0,
        'ultimo_ano': 'Sem Dados',
        'ultimo_mes': 'Sem Dados',
        
        # Financial Metrics
        'total_valor_vendido_filtrado': 0,
        'total_clientes_filtrado': 0,
        'ticket_medio_filtrado': 0,
        'total_follow_ups': 0,
        'total_entrada': 0,
        'percent_entrada': 0,

        
        # Unit Type Variables
        'quant_integral': 0,
        'percent_integral': 0,
        'quant_4_semanas': 0,
        'percent_4_semanas': 0,
        'quant_6_semanas': 0,
        'percent_6_semanas': 0,
        'quant_13_semanas': 0,
        'percent_13_semanas': 0,
        
        # Discount Variables
        'total_desconto_financeiro': 0,
        'percent_desconto_financeiro': 0,
        'total_desconto_viabilidade': 0,
        'percent_desconto_viabilidade': 0,
        'total_ganho_viabilidade': 0,
        'percent_ganho_viabilidade': 0,
        
        # Client Variables
        'total_clientes': 0,
        
        # Formatted Values
        'total_desconto_financeiro_formatado': "R$ 0,00",
        'total_desconto_viabilidade_formatado': "R$ 0,00",
        'total_ganho_viabilidade_formatado': "R$ 0,00"
    }

# Initialize variables at the start of your script
vars = initialize_variables()


# After your imports...

# Initialize variables
vars = initialize_variables()

# ============================


# ✅ Caminho do arquivo (CSV ou XLSX)
#caminho_arquivo = r"BASERESGATE.xlsx"  # Altere o caminho aqui

# ============================
# 🔹 EXECUÇÃO
# ============================
#df = load_data(caminho_arquivo)

# ============================
# 🔹 EXIBIR O DATAFRAME
# ============================
#if not df.empty:
 #   st.title("📊")
    # st.dataframe(df)
#else:
#    st.error("⚠️ Não foi possível carregar o DataFrame. Verifique o arquivo.")









# Criando o sidebar de navegação
st.sidebar.title('Navegação')
pagina = st.sidebar.radio('Selecione a página:', [
    'HOME',
    'RANKING',
    'Origens_Estados',
    'GRÁFICOS VIABILIDADE',
    'GRÁFICOS TABELA',
    'GRÁFICOS DISTRATOS',
    'Previsão de Vendas',
    'Simulador'
])

# Criando seção de filtros no sidebar
st.sidebar.title('Filtros')

# Convertendo a coluna 'Data da Venda' para datetime
df['Data da Venda'] = pd.to_datetime(df['Data da Venda'], errors='coerce')

# Determinando o primeiro e o último dia de venda
# Definindo limite inferior para 2020
data_inicio_min = pd.to_datetime('2022-08-05').date()
# Definindo limite superior para 2027
data_fim_max = pd.to_datetime('2025-12-31').date()

# Valores padrão para o filtro (pode ser ajustado conforme necessidade)
data_inicio_padrao = pd.to_datetime('2022-08-05').date()
data_fim_padrao = pd.to_datetime('2025-12-31').date()

# Filtro de data com os novos limites
data_inicio = st.sidebar.date_input(
    'Data da Venda - Início',
    min_value=data_inicio_min,
    max_value=data_fim_max,
    value=data_inicio_padrao
)

data_fim = st.sidebar.date_input(
    'Data da Venda - Fim',
    min_value=data_inicio_min,
    max_value=data_fim_max,
    value=data_fim_padrao
)

# Filtrando o DataFrame com as datas selecionadas
df_filtrado = df[(df['Data da Venda'].dt.date >= data_inicio)
                 & (df['Data da Venda'].dt.date <= data_fim)]

# Demais filtros
gerente = st.sidebar.selectbox(
    'GERENTE', ['Todos'] + list(df['GERENTE'].unique()))
corretor1 = st.sidebar.selectbox(
    'Corretor 1', ['Todos'] + list(df['Corretor 1'].unique()))
corretor2 = st.sidebar.selectbox(
    'Corretor 2', ['Todos'] + list(df['Corretor 2'].unique()))
produto = st.sidebar.selectbox(
    'PRODUTO', ['Todos'] + list(df['PRODUTO'].unique()))
uf = st.sidebar.selectbox('UF', ['Todos'] + list(df['UF'].unique()))
origem_venda = st.sidebar.selectbox(
    'Origem da venda', ['Todos'] + list(df['Origem da venda'].unique()))
campanha = st.sidebar.selectbox(
    'Campanha', ['Todos'] + list(df['Campanha'].unique()))
status1 = st.sidebar.selectbox(
    'Status 1', ['Todos'] + list(df['Status 1'].unique()))
status2 = st.sidebar.selectbox(
    'Status 2', ['Todos'] + list(df['Status 2'].unique()))
tipo_unidade = st.sidebar.selectbox('Tipo unidade (semanas)', [
                                    'Todos'] + list(df['Tipo unidade semanas'].unique()))

# Aplicando os filtros
df_filtrado = df.copy()

# Título
st.markdown(
    f"""
    <h1 style='font-size: 24px; text-align: center;'>
        📊 Análise de Vendas
    </h1>
    """,
    unsafe_allow_html=True
)

# Criar uma lista para armazenar os filtros aplicados
filtros_aplicados = []

# Filtro de data
mask_data = (df_filtrado['Data da Venda'].dt.date >= data_inicio) & (
    df_filtrado['Data da Venda'].dt.date <= data_fim)
df_filtrado = df_filtrado[mask_data]

# Adiciona o filtro de data na lista
filtros_aplicados.append(f"📅 **Período:** {data_inicio} - {data_fim}")

# Aplicar os filtros e armazenar os selecionados
if gerente != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['GERENTE'] == gerente]
    filtros_aplicados.append(f"👤 **Gerente:** {gerente}")

if corretor1 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Corretor 1'] == corretor1]
    filtros_aplicados.append(f"🏠 **Corretor 1:** {corretor1}")

if corretor2 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Corretor 2'] == corretor2]
    filtros_aplicados.append(f"🏠 **Corretor 2:** {corretor2}")

if produto != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['PRODUTO'] == produto]
    filtros_aplicados.append(f"📦 **Produto:** {produto}")

if uf != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['UF'] == uf]
    filtros_aplicados.append(f"🌎 **UF:** {uf}")

if origem_venda != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Origem da venda'] == origem_venda]
    filtros_aplicados.append(f"💼 **Origem da Venda:** {origem_venda}")

if campanha != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Campanha'] == campanha]
    filtros_aplicados.append(f"🎯 **Campanha:** {campanha}")

if status1 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Status 1'] == status1]
    filtros_aplicados.append(f"✅ **Status 1:** {status1}")

if status2 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Status 2'] == status2]
    filtros_aplicados.append(f"🔄 **Status 2:** {status2}")

if tipo_unidade != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas'] == tipo_unidade]
    filtros_aplicados.append(f"🏢 **Tipo Unidade:** {tipo_unidade}")

# Exibir os filtros aplicados na parte superior
if filtros_aplicados:
    st.markdown(
        f"""
        <h3 style='font-size: 18px; text-align: center;'>
            🎛️ **Filtros Aplicados:**
        </h3>
        <p style='text-align: center;'>{' | '.join(filtros_aplicados)}</p>
        """,
        unsafe_allow_html=True
    )

# ============================ HOME ============================
if pagina == 'HOME':
    #Sst.title('🏠 Página Home')
    if not df_filtrado.empty:
        #st.write("### Análise de Valores Vendidos")
        #st.write(df_filtrado)

        ####################################### BEGIN HOME############################################################
        ####################################################################################################
        # Filtrando apenas registros onde 'Status 1' é "ASSINADO" e 'Status 2' é "ATIVO"
        df_assinado = df_filtrado[(df_filtrado['Status 1'] == 'ASSINADO') & (df_filtrado['Status 2'] == 'ATIVO')]

        # Filtrando apenas registros com "# Clientes" igual a 1 e que também atendem a condição anterior
        df_assinado_Cliente = df_filtrado[(df_filtrado['Status 1'] == 'ASSINADO') & 
                                        (df_filtrado['Status 2'] == 'ATIVO')]

        # Contar a quantidade de registros com as novas condições aplicadas
        quant_assinado = df_assinado.shape[0]
        quant_assinado_Cliente = df_assinado_Cliente.shape[0]

            # Filtrando os dados para excluir as linhas onde "Status 2" seja "CANCELADO" ou "UPGRADE"
        #df_filtrado_sem_cancelado = df_filtrado[df_filtrado['Status 2'].isin(['CANCELADO', 'CANCELADO UPGRADE'])]

        # Calculando o total da coluna "Valor vendido" sem os registros "CANCELADO" e "UPGRADE"
        #VGV_BRUTO = df_filtrado_sem_cancelado['Valor vendido'].sum()

#___________________________________________________________________________________
#  
        VGV_BRUTO = df_filtrado[df_filtrado['Status 2'] == 'ATIVO']['Valor vendido'].sum()
        DESCONTO_REAL_VIABILIDADE = df_filtrado[df_filtrado['Status 2'] == 'ATIVO']['Desconto Real Viabilidade'].sum()

                # Calcula o percentual diretamente
        percentual_desconto_real_viabilidade = (
            df_filtrado[df_filtrado['Status 2'] == 'ATIVO']['Desconto Real Viabilidade'].sum() / 
            df_filtrado['Valor vendido'].sum() * 100
        ) if df_filtrado['Valor vendido'].sum() > 0 else 0

      

        # 1) Converter a coluna Desconto Financeiro para tipo numérico
        df_filtrado['Desconto Financeiro'] = pd.to_numeric(df_filtrado['Desconto Financeiro'], errors='coerce')

        # 2) (Opcional) Substituir valores NaN por 0, se fizer sentido na sua regra de negócio
        df_filtrado['Desconto Financeiro'].fillna(0, inplace=True)

        # 3) Converter 'Valor vendido' para numérico também (caso necessário)
        df_filtrado['Valor vendido'] = pd.to_numeric(df_filtrado['Valor vendido'], errors='coerce')
        df_filtrado['Valor vendido'].fillna(0, inplace=True)

        # 4) Calcular o VGV_LIQUIDO, somando:
        #    - todos os 'Valor vendido' de Status 2 = 'ATIVO'
        #    - mais os 'Desconto Financeiro' daqueles que têm Status 2 = 'ATIVO' e Desconto > 0
        VGV_LIQUIDO = (
            df_filtrado.loc[df_filtrado['Status 2'] == 'ATIVO', 'Valor vendido'].sum()
            + df_filtrado.loc[
                (df_filtrado['Status 2'] == 'ATIVO') & (df_filtrado['Desconto Financeiro'] > 0),
                'Desconto Financeiro'
            ].sum()
        )



        # Converter "Desconto Financeiro" para numérico
        df_filtrado['Desconto Financeiro'] = pd.to_numeric(
            df_filtrado['Desconto Financeiro'], errors='coerce'
        )
        # Substituir NaN por 0
        df_filtrado['Desconto Financeiro'].fillna(0, inplace=True)

        # Filtra apenas as linhas onde Desconto Financeiro > 0
        df_temp = df_filtrado.loc[
            df_filtrado['Desconto Financeiro'] > 0,
            ['Valor vendido', 'Desconto Financeiro']
        ].copy()

        # Calcula o valor líquido linha a linha
        df_temp['liquido'] = df_temp['Valor vendido'] - df_temp['Desconto Financeiro']

        # Desconsidera valores negativos, forçando mínimo a 0
        df_temp['liquido'] = df_temp['liquido'].clip(lower=0)

        # Soma o valor líquido total
        #VGV_LIQUIDO = df_temp['liquido'].sum()


        #VGV_REALIZADO = VGV_BRUTO - VGV_LIQUIDO
# 
# 
# 
# ____________________________________________________________________________



        # Definir as variáveis novamente para garantir que estão corretamente inicializadas
        total_valor_vendido = df_filtrado['Valor vendido'].sum()
        total_status1_nao_assinado = df_filtrado['Status 1'].value_counts().get('NAO ASSINADO', 0)

        # Criar a variável que calcula o total de valor vendido dividido pelo total de não assinados
        if total_status1_nao_assinado != 0:  # Evita divisão por zero
            vgv_total_bruto_por_pendente_assinatura = total_valor_vendido / total_status1_nao_assinado
        else:
            vgv_total_bruto_por_pendente_assinatura = 0  # Define 0 caso não haja pendentes de assinatura

                # Exibir o valor da nova variável
           


#___________________________________________________________________________________



 ####################################################################################################
        # Calculando o total das vendas

        # Filtrar somente os valores "Assinado" na coluna "Status 1"
        df_nao_assinado = df_filtrado[df_filtrado['Status 1'] == 'NAO ASSINADO']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_nao_assinado = df_assinado.shape[0]

        # Filtrando os dados para excluir as linhas com 'CANCELADO' em "Status 2"
        #df_filtrado_sem_cancelado = df_filtrado[df_filtrado['Status 2'] != 'CANCELADO']

        # Calculando o total da coluna "Valor vendido" sem os "CANCELADO"
        #VGV_BRUTO = df_filtrado_sem_cancelado['Valor vendido'].sum(
       # )

#___________________________________________________________________________________





        # Converter a coluna "Desconto Financeiro" para numérico, substituindo erros por NaN
      #  df_filtrado_sem_cancelado['Desconto Financeiro'] = pd.to_numeric(
       #     df_filtrado_sem_cancelado['Desconto Financeiro'], errors='coerce'
       # )

        # Substituir NaN por 0 para evitar erro na soma
       # df_filtrado_sem_cancelado['Desconto Financeiro'].fillna(0, inplace=True)

        # Agora podemos calcular a soma sem erro
       # total_desconto_financeiro_sem_cancelado = df_filtrado_sem_cancelado['Desconto Financeiro'].sum()

        # Exibir o resultado no Streamlit
        #st.write(f"💰 Total de Desconto Financeiro (sem cancelados): R$ {total_desconto_financeiro_sem_cancelado:,.2f}")


#___________________________________________________________________________________

        # Calculando o valor final descontando o "Desconto Financeiro"
     #  valor_final = VGV_BRUTO - \
       #     total_desconto_financeiro_sem_cancelado

        # _________________________________________________________________________________________#

        df_nao_assinado = df_filtrado[df_filtrado['Status 1']
                                      == 'NAO ASSINADO']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_nao_assinado = df_nao_assinado.shape[0]

        # _________________________________________________________________________________________#







        # Supondo que df_filtrado já existe e contém a coluna "Latencia de compra"

        # 1. Converter a coluna "Latencia de compra" para numérico
        df_filtrado['Latencia de compra'] = pd.to_numeric(df_filtrado['Latencia de compra'], errors='coerce')

        # 2. Filtrar os valores válidos (remover valores nulos ou inválidos)
        latencia_compra = df_filtrado['Latencia de compra'].dropna()

        # 3. Calcular a média
        if not latencia_compra.empty:  # Verifica se há valores válidos
            media_latencia_compra = latencia_compra.mean()
        else:
            media_latencia_compra = 0  # Define a média como 0 se não houver valores válidos

        # 4. Arredondar a média
        media_latencia_compra_arredondada = round(np.nan_to_num(media_latencia_compra, nan=0))

        # 5. Exibir o resultado no Streamlit
        #st.write(f"Média da latência de compra: {media_latencia_compra_arredondada}")

        # Mensagem de aviso se não houver valores válidos
        if latencia_compra.empty:
            st.warning("Não há valores válidos de latência de compra para calcular a média.")








        # Criar o histograma
        fig, ax = plt.subplots(figsize=(12, 6))  # Tamanho do gráfico ajustado
        plt.hist(latencia_compra, bins=30, color='blue', edgecolor='black')
        plt.title('Distribuição da Latencia de compra')
        plt.xlabel('Latencia de compra (dias)')
        plt.ylabel('Frequência')
        plt.grid(True)

        # Salvar o gráfico em uma imagem
        buf = io.BytesIO()  # Agora 'io' está importado
        fig.savefig(buf, format="png")
        buf.seek(0)

        # _________________________________________________________________________________________#


###########################################tabela_avista############################################
        df_a_vista = df_filtrado[df_filtrado['Tabela'] == 'A vista']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_a_vista = df_a_vista.shape[0]


        # Aplicar as três condições na mesma expressão
        tabela_avista = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tabela'] == 'A vista')
        ].shape[0]



        # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_avista = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tabela'] == 'A vista')
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0



        # Aplicar as três condições na mesma expressão
        tabela_curta = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tabela'] == 'Curta')
        ].shape[0]



                # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_curta = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tabela'] == 'Curta')
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0



                # Aplicar as três condições na mesma expressão
        tabela_longa = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tabela'] == 'Longa')
        ].shape[0]


                # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_longa = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tabela'] == 'Longa')
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0



                # Aplicar as três condições na mesma expressão
        tabela_longuissima = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tabela'] == 'Longuissima')
        ].shape[0]



                # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_longuissima = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tabela'] == 'Longuissima')
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0




                # Aplicar as três condições na mesma expressão
        tabela_integral = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tipo unidade semanas'] == 'Integral')& 
            (df_filtrado['# Clientes'] == 1)
        ].shape[0]


                # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_Integral = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tipo unidade semanas'] == 'Integral')& 
                (df_filtrado['# Clientes'] == 1)
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0


                # Aplicar as três condições na mesma expressão
        tabela_quatro_semanas = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tipo unidade semanas'] == 4)& 
            (df_filtrado['# Clientes'] == 1)
        ].shape[0]


                # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_quatro_semanas = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tipo unidade semanas'] == 4)& 
                (df_filtrado['# Clientes'] == 1)
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0


                # Aplicar as três condições na mesma expressão
        tabela_seis_semanas = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tipo unidade semanas'] == 6)& 
            (df_filtrado['# Clientes'] == 1)
        ].shape[0]


                # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_seis_semanas = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tipo unidade semanas'] == 6)& 
                (df_filtrado['# Clientes'] == 1)
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0



                # Aplicar as três condições na mesma expressão
        tabela_treze_semanas = df_filtrado[
            (df_filtrado['Status 1'] == 'ASSINADO') & 
            (df_filtrado['Status 2'] == 'ATIVO') & 
            (df_filtrado['Tipo unidade semanas'] == 13)& 
            (df_filtrado['# Clientes'] == 1)
        ].shape[0]


                # Calcula o percentual diretamente e armazena na variável
        percentual_tabela_treze_semanas = (
            df_filtrado[
                (df_filtrado['Status 1'] == 'ASSINADO') & 
                (df_filtrado['Status 2'] == 'ATIVO') & 
                (df_filtrado['Tipo unidade semanas'] == 13)& 
                (df_filtrado['# Clientes'] == 1)
            ].shape[0] / df_filtrado.shape[0] * 100
        ) if df_filtrado.shape[0] > 0 else 0




###########################################################################################


        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_a_vista = round((quant_a_vista / total_registros) * 100)
        percent_a_vista = round(
            (quant_a_vista / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_curta = df_filtrado[df_filtrado['Tabela'] == 'Curta']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_curta = df_curta.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_curta = round((quant_curta / total_registros) * 100)
        percent_curta = round((quant_curta / total_registros)
                              * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_longa = df_filtrado[df_filtrado['Tabela'] == 'Longa']
        df_longa = df_filtrado[df_filtrado['Tabela'] == 'Longa']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_longa = df_longa.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_longa = round((quant_longa / total_registros) * 100)
        percent_longa = round((quant_longa / total_registros)
                              * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_longuissima = df_filtrado[df_filtrado['Tabela'] == 'Longuissima']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        df_longuissima = df_filtrado[df_filtrado['Tabela'] == 'Longuissima']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_longuissima = df_longuissima.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_longuissima = round((quant_longuissima / total_registros) * 100)
        percent_longuissima = round(
            (quant_longuissima / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_filtrado['Data da Venda'] = pd.to_datetime(
            df_filtrado['Data da Venda'])

        # 1️⃣ Criar colunas para Ano e Mês
        df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year
        df_filtrado['Mês'] = df_filtrado['Data da Venda'].dt.month

        # 2️⃣ Agrupar por Ano e Mês para calcular o total de vendas
        total_por_mes = df_filtrado.groupby(
            ['Ano', 'Mês'])['Valor vendido'].sum().reset_index()

        # 3️⃣ Ordenar os dados por Ano e Mês
        total_por_mes = total_por_mes.sort_values(
            ['Ano', 'Mês']).reset_index(drop=True)

        # 4️⃣ Calcular a variação percentual mês a mês
        total_por_mes['Variação (%)'] = total_por_mes['Valor vendido'].pct_change(
        ) * 100  # Em percentual

        # Adicionar coluna de setas com códigos HTML para cor
        def definir_seta_colorida(variacao):
            if pd.isna(variacao):
                return '<span style="color:gray; font-size:25px;">➡️</span>'  # Estabilidade inicial
            elif variacao > 0:
                return '<span style="color:green; font-size:25px;">⬆️</span>'  # Crescimento
            elif variacao < 0:
                return '<span style="color:red; font-size:25px;">⬇️</span>'    # Queda
            else:
                return '<span style="color:gray; font-size:25px;">➡️</span>'  # Estabilidade

        total_por_mes['Seta'] = total_por_mes['Variação (%)'].apply(
            definir_seta_colorida)

        # 6️⃣ Converter o número do mês para nome
        total_por_mes['Mês Nome'] = total_por_mes['Mês'].apply(
            lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))

        # 7️⃣ Valores para o Cartão
        valor_final = df_filtrado['Valor vendido'].sum()  # VGV Bruto
        quant_assinado = df_filtrado.shape[0]  # Total de assinados

        # Últimos dados para o cartão
        if not total_por_mes.empty:
            ultima_variacao = total_por_mes.iloc[-1]['Seta']
            ultimo_valor = total_por_mes.iloc[-1]['Valor vendido']
            ultimo_ano = total_por_mes.iloc[-1]['Ano']
            ultimo_mes = total_por_mes.iloc[-1]['Mês Nome']
        else:
            # Valores padrão em caso de DataFrame vazio
            ultima_variacao = '➡️'
            ultimo_valor = 0
            ultimo_ano = 'Sem Dados'
            ultimo_mes = 'Sem Dados'

            # ____
            # _____________________________________________________________________________________#

            # Converter colunas para numérico e tratar valores ausentes no DataFrame filtrado
        df_filtrado['Valor vendido'] = pd.to_numeric(
            df_filtrado['Valor vendido'], errors='coerce')
        df_filtrado['# Clientes'] = pd.to_numeric(
            df_filtrado['# Clientes'], errors='coerce')

        # Calcular o Ticket Médio usando o DataFrame filtrado
        total_valor_vendido_filtrado = df_filtrado['Valor vendido'].sum()
       

        # Garantir que a coluna "# Clientes" seja numérica e remover valores inválidos
        df_filtrado["# Clientes"] = pd.to_numeric(df_filtrado["# Clientes"], errors="coerce").fillna(0)

        # Filtrar apenas registros onde "# Clientes" é igual a 1 e "Status 2" é "ATIVO"
        df_clientes_validos = df_filtrado[(df_filtrado["# Clientes"] == 1) & (df_filtrado["Status 2"] == "ATIVO")]

        # Contar quantos clientes atendem a essa condição
        total_clientes_filtrado = df_clientes_validos["# Clientes"].count()

        # Evitar divisão por zero
        if total_clientes_filtrado != 0:
            ticket_medio_filtrado = total_valor_vendido_filtrado / total_clientes_filtrado
        else:
            ticket_medio_filtrado = 0

            # _____________________________________________________________________________________#

            # Converter a coluna 'N de FU' para numérico no DataFrame filtrado
        df_filtrado['N de FU'] = pd.to_numeric(
            df_filtrado['N de FU'], errors='coerce')

        # Calcular o total de Follow-ups (ignorando valores nulos)
        total_follow_ups = df_filtrado['N de FU'].sum()

        # Remover casas decimais usando int()
        total_follow_ups = int(total_follow_ups)

        # _____________________________________________________________________________________#

        # _____________________________________________________________________________________#

        # Converter a coluna 'N de FU' para numérico no DataFrame filtrado
        df_filtrado['De Entrada'] = pd.to_numeric(
            df_filtrado['De Entrada'], errors='coerce')

        # Calcular o total de Follow-ups (ignorando valores nulos)
        total_entrada = df_filtrado['De Entrada'].sum()

        # Remover casas decimais usando int()
        total_entrada = int(total_entrada)

        percent_entrada = round((total_entrada / VGV_BRUTO)
                                * 100) if VGV_BRUTO != 0 else 0

        # _____________________________________________________________________________________#
        # _________________________________________________________________________________________#

        df_integral = df_filtrado[df_filtrado['Tipo unidade semanas'] == 'Integral']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_integral = df_integral.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_a_vista = round((quant_a_vista / total_registros) * 100)
        percent_integral = round(
            (quant_integral / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        # Normalizando os dados para garantir que o filtro funcione
        df_filtrado['Tipo unidade semanas'] = df_filtrado['Tipo unidade semanas'].astype(
            str).str.strip()

        # Agora filtra
        df_4_semanas = df_filtrado[df_filtrado['Tipo unidade semanas'] == '4']
        quant_4_semanas = df_4_semanas.shape[0]
        total_registros = df_filtrado.shape[0]
        percent_4_semanas = round(
            (quant_4_semanas / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        # _________________________________________________________________________________________#

        # Normalizando os dados para garantir que o filtro funcione
        df_filtrado['Tipo unidade semanas'] = df_filtrado['Tipo unidade semanas'].astype(
            str).str.strip()

        # Agora filtra
        df_6_semanas = df_filtrado[df_filtrado['Tipo unidade semanas'] == '6']
        quant_6_semanas = df_6_semanas.shape[0]
        total_registros = df_filtrado.shape[0]
        percent_6_semanas = round(
            (quant_6_semanas / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        # _________________________________________________________________________________________#

        # Normalizando os dados para garantir que o filtro funcione
        df_filtrado['Tipo unidade semanas'] = df_filtrado['Tipo unidade semanas'].astype(
            str).str.strip()

        # Agora filtra
        df_13_semanas = df_filtrado[df_filtrado['Tipo unidade semanas'] == '13']
        quant_13_semanas = df_13_semanas.shape[0]
        total_registros = df_filtrado.shape[0]
        percent_13_semanas = round(
            (quant_13_semanas / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#
        # _____________________________________________________________________________________#

        # Converter a coluna 'Desconto Financeiro' para numérico no DataFrame filtrado
        df_filtrado['Desconto Financeiro'] = pd.to_numeric(
            df_filtrado['Desconto Financeiro'], errors='coerce')

        # Calcular o total de Desconto Financeiro (ignorando valores nulos)
        total_desconto_financeiro = df_filtrado['Desconto Financeiro'].sum()

        # Calcular o percentual sobre o total vendido (em %)
        percent_desconto_financeiro = round(
            (total_desconto_financeiro / VGV_BRUTO) * 100) if VGV_BRUTO != 0 else 0

        # Formatar o valor em reais (usando substituição para vírgula e ponto)
        total_desconto_financeiro_formatado = "R$ {:,.2f}".format(
            total_desconto_financeiro).replace(",", "X").replace(".", ",").replace("X", ".")

        # _____________________________________________________________________________________#
        # ______#_____________________________________________________________________________________#

        # Converter a coluna 'Desconto Financeiro' para numérico no DataFrame filtrado
        df_filtrado['Desconto Real Viabilidade'] = pd.to_numeric(
            df_filtrado['Desconto Real Viabilidade'], errors='coerce')

        # Calcular o total de Desconto Financeiro (ignorando valores nulos)
        total_desconto_viabilidade = df_filtrado['Desconto Real Viabilidade'].sum(
        )

        # Calcular o percentual sobre o total vendido (em %)
        percent_desconto_viabilidade = round(
            (total_desconto_viabilidade / VGV_BRUTO) * 100) if VGV_BRUTO != 0 else 0

        # Formatar o valor em reais (usando substituição para vírgula e ponto)
        total_desconto_viabilidade_formatado = "R$ {:,.2f}".format(
            total_desconto_viabilidade).replace(",", "X").replace(".", ",").replace("X", ".")

        # _____________________________________________________________________________________#
        # Converter a coluna 'Desconto Financeiro' para numérico no DataFrame filtrado
        df_filtrado['Ganho Viabilidade'] = pd.to_numeric(
            df_filtrado['Ganho Viabilidade'], errors='coerce')

        # Calcular o total de Desconto Financeiro (ignorando valores nulos)
        total_ganho_viabilidade = df_filtrado['Ganho Viabilidade'].sum()

        # Calcular o percentual sobre o total vendido (em %)
        percent_ganho_viabilidade = round(
            (total_ganho_viabilidade / VGV_BRUTO) * 100) if VGV_BRUTO != 0 else 0

        # Formatar o valor em reais (usando substituição para vírgula e ponto)
        total_ganho_viabilidade_formatado = "R$ {:,.2f}".format(
            total_ganho_viabilidade).replace(",", "X").replace(".", ",").replace("X", ".")

        # _____________________________________________________________________________________#


            # Filtrar os registros onde "Status 1" é "ASSINADO" e "Status 2" é "CANCELADO"
        df_distrato = df_filtrado[(df_filtrado["Status 1"] == "ASSINADO") & (df_filtrado["Status 2"] == "CANCELADO")]

        # Somar os valores da coluna "Valor vendido" para esses registros
        distrato_valor = df_distrato["Valor vendido"].sum()
     



       


            # Filtrar os registros onde "Status 1" é "ASSINADO" e "Status 2" é "CANCELADO"
        df_distrato_up_grade = df_filtrado[(df_filtrado["Status 1"] == "ASSINADO") & (df_filtrado["Status 2"] == "CANCELADO UPGRADE")]

        # Somar os valores da coluna "Valor vendido" para esses registros
        distrato_valor_up_grade = df_distrato_up_grade["Valor vendido"].sum()

        # Calcular o percentual do valor "CANCELADO UPGRADE" em relação ao total de "ASSINADO + CANCELADO"
        percentual_distrato_up_grade = (distrato_valor_up_grade / distrato_valor) * 100 if distrato_valor > 0 else 0

        # Calcular o percentual do valor "CANCELADO UPGRADE" em relação ao total de "CANCELADO"
        percentual_distrato_upgrade_sobre_cancelado = (distrato_valor_up_grade / distrato_valor) * 100 if distrato_valor > 0 else 0


        # Arredondar o percentual para um número inteiro
        percentual_distrato_upgrade_sobre_cancelado = int(percentual_distrato_upgrade_sobre_cancelado)

        percentual_distrato_up_grade = int(percentual_distrato_up_grade)


        # Somar a coluna "De Entrada"
        # Converter a coluna "% De Entrada" para numérico
        #df["De Entrada"] = pd.to_numeric(df["De Entrada"], errors="coerce")

        # Somar a coluna "% De Entrada"
        #soma_percentual_entrada = df["De Entrada"].sum()



        # Converter a coluna "% De Entrada" para numérico
        df_filtrado["De Entrada"] = pd.to_numeric(df_filtrado["De Entrada"], errors="coerce")

        # Somar a coluna "% De Entrada"
        soma_percentual_entrada = df_filtrado["De Entrada"].sum()

###################################TICEKET MEDIO################################
        VGV_BRUTO = df_filtrado[df_filtrado['Status 2'] == 'ATIVO']['Valor vendido'].sum()
        


                # Verifica se total_clientes_filtrado é maior que zero para evitar divisão por zero
            
            # Se df_clientes_validos for um DataFrame, conte o número de clientes válidos
        total_clientes_validos = df_clientes_validos.shape[0]  # Número de linhas no DataFrame

        # Calcule o Ticket Médio
        if total_clientes_validos > 0:
            TICKET_MEDIO = VGV_LIQUIDO / total_clientes_validos
        else:
            TICKET_MEDIO = 0  # Evita divisão por zero
        

      


###################################DISTRATO#####################################

            # Calcular Distrato (Assinado + Cancelado)
        distrato = df_filtrado[(df_filtrado['Status 1'] == 'ASSINADO') & 
                                (df_filtrado['Status 2'].isin(['CANCELADO']))].shape[0]
        

        # Calcular Distrato Upgrade (Assinado + Cancelado Upgrade)
        distrato_upgrade = df_filtrado[(df_filtrado['Status 1'] == 'ASSINADO') & 
                                    (df_filtrado['Status 2'] == 'CANCELADO UPGRADE')].shape[0]
################################################################################

        # Exibir o resultado
        #print(f"Soma da coluna 'De Entrada': {soma_percentual_entrada:.2f}%")
        # Remover valores nulos antes da análise
        #df_percentual_entrada = df_filtrado["De Entrada"].dropna()

        # Analisar os valores da coluna "De Entrada" sem filtros adicionais
        #percentual_entrada_descricao_filtrado = {
            #df_percentual_entrada.mean(),
            #"Mediana": df_percentual_entrada.median(),
           # "Mínimo": df_percentual_entrada.min(),
           # "Máximo": df_percentual_entrada.max(),
           # "Desvio Padrão": df_percentual_entrada.std()
        #}

        #percentual_entrada_descricao_filtrado = int(percentual_entrada_descricao_filtrado)

        #percentual_media_inteiro = int(percentual_entrada_descricao_filtrado["Média"])
        #percentual_entrada_descricao_filtrado = {key: int(value) for key, value in percentual_entrada_descricao_filtrado.items()}
        #percentual_entrada_descricao_filtrado = {key: int(value) for key, value in percentual_entrada_descricao_filtrado.items()}
        #percentual_entrada_descricao_filtrado = dict(percentual_entrada_descricao_filtrado)


        # _____________________________________________________________________________________#

        # _____________________________________________________________________________________#

        # Agrupando por 'CLIENTES' e contando a quantidade de registros para cada cliente
        # clientes_agrupados = df.groupby('CLIENTE').size().reset_index(name='Total')
        # Agrupando por 'CLIENTES' e contando a quantidade de registros para cada cliente
        # Contando o número de clientes distintos
        # Agora o total_clientes irá variar com os filtros aplicados
        # Contando os clientes únicos no df_filtrado
        #total_clientes = df_filtrado['# Clientes'].nunique()
   # Somar os valores maiores que 0 na coluna "# Clientes"
        # Somar apenas os valores maiores que 0 na coluna "# Clientes"
        
        #soma_clientes_coluna



        Ticket = VGV_LIQUIDO / total_clientes_filtrado

        ###################################################################################################
        ####################################################################################################

        # CSS para padronizar o tamanho dos cartões
        st.markdown(
            """
<style>
    .card {
     
        padding: 20px; /* Reduzi o padding para diminuir o espaçamento interno */
        width: 90%;
        height: 130px; /* Altura fixa para todos os cartões */
        margin-right: 15px;
        text-align: center;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center; /* Centraliza verticalmente */
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* Adiciona sombra */
        color: white; 
        font-size: 14px; 
        font-weight: bold;
    }

    .card span {
        margin: 2px 0; /* Reduzi o espaçamento entre os textos */
        color: black; /* Cor do texto */
        font-weight: bold; /* Texto em negrito */
    }
</style>
                """,
            unsafe_allow_html=True
        )

        # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#fff;">
                    <span style="color: black; font-size: 15px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Primeira linha de cartões
            st.write("")  # Linha em branco cria espaço
            # Criando as colunas para os cartões
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:

                    # Função de formatação
                    def formatar_br(VGV_BRUTO):
                            return f"R$ {VGV_BRUTO:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    # Função de formatação
                    def formatar_br(ultimo_valor):
                            return f"R$ {ultimo_valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") 
                             # Função de formatação
                    def formatar_br(valor_final):
                            return f"R$ {valor_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") 
                    def formatar_br(ticket_medio_filtrado):
                            return f"R$ {ticket_medio_filtrado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    def formatar_br(total_desconto_financeiro):
                            return f"R$ {total_desconto_financeiro:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") 
                    def formatar_br(total_desconto_viabilidade):
                            return f"R$ {total_desconto_viabilidade:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") 
                    def formatar_br(total_ganho_viabilidade):
                            return f"R$ {total_ganho_viabilidade:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    def formatar_br(vgv_total_bruto_por_pendente_assinatura):
                            return f"R$ {vgv_total_bruto_por_pendente_assinatura:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    #____________________________________________________________________
                    total_status1_assinado = df_filtrado['Status 1'].value_counts().get('ASSINADO', 0)
                    #____________________________________________________________________
                    def formatar_br(distrato_valor):
                            return f"R$ {distrato_valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

                    def formatar_br(distrato_valor_up_grade):
                            return f"R$ {distrato_valor_up_grade:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    def formatar_br(VGV_LIQUIDO):
                            return f"R$ {VGV_LIQUIDO:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    def formatar_br(VGV_REALIZADO):
                            return f"R$ {VGV_REALIZADO:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    def formatar_br(DESCONTO_REAL_VIABILIDADE):
                            return f"R$ {DESCONTO_REAL_VIABILIDADE:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


              
#<span style="font-size: 8px;">R$ {formatar_br(ultimo_valor)}</span>
#<span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">Mês: {ultimo_mes} - Ano: {ultimo_ano}</span>
#<span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">{ultima_variacao}</span>
                    st.markdown(
                    f"""
                            <div class="card" style="background-color:#32CD32">
                                <span style="color: white; font-size: 1vw; font-weight: bold;">💰 VGV Total Bruto</span>
                                <span style="color: white; font-size: 1vw; font-weight: bold;">Total Assinados: {quant_assinado}</span>
                                <span style="color: white; font-size: 1vw; font-weight: bold;">{formatar_br(VGV_LIQUIDO)}</span>

                            </div>
                                                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#32CD32">
                            <span style="color: white; font-size: 14px; font-weight: bold;">💰 VGV Total Bruto</span>
                             <span style="font-size: 18px; color: white;">Pendente Assinatura: {quant_nao_assinado}</span>
                            <span style="font-size: 20px; color: white;">{formatar_br(VGV_LIQUIDO)}</span>
                           
                            
                            
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;"> 👥Quantidade Clientes</span>
                            <span style="font-size: 20px; color: white;">{total_clientes_filtrado}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col4:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#12172b">
                            <span style="font-size: 20px; color: white;font-size:14px;font-weight:bold;">📉 Latência de compra</span>
                            <span style="font-size: 20px; color: white;">{media_latencia_compra_arredondada} Dias</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col5:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">TABELA A VISTA (4M)</span>
                            <span style="font-size: 20px; color: white;">{tabela_avista}</span>
                            <span style="font-size: 20px; color: white;">{percentual_tabela_avista:.2f}%</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )
            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço
            # Segunda linha de cartões
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">VGV TOTAL LÍQUIDO</span>
                            <span style="font-size: 20px; color: white; font-size: 20px;">R$ {formatar_br(VGV_BRUTO)}</span>
                            
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#32CD32">
                            <span style="color: white; font-size: 14px; font-weight: bold;">VGV Total Liquido</span>
                            <span style="font-size: 14px; color: white;">R$ {formatar_br(VGV_BRUTO)}</span>
                            <span style="font-size: 20px; color: white;">Total Assinados: {quant_assinado_Cliente}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">Ticket Médio</span>
                            <span style="font-size: 20px; color: white;">{formatar_br(Ticket)}</span>
                            
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col4:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#12172b">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">Follow-ups</span>
                            <span style="font-size: 20px; color: white;">{total_follow_ups}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col5:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">TABELA CURTA (35M)</span>
                            <span style="font-size: 20px; color: white;">{tabela_curta}</span>
                            <span style="font-size: 20px; color: white;">{percentual_tabela_curta:.2f}%</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#fff;">
                    <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📊 DESCONTOS FINANCEIROS</span>
                        <span style="font-size: 20px; color: white;">R$ {formatar_br(total_desconto_financeiro)}</span>
                        <span style="font-size: 20px; color: white;">{percent_desconto_financeiro:.2f}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📆INTEGRAL</span>
                            <span style="font-size: 20px; color: white;">{tabela_integral}</span>
                            <span style="font-size: 20px; color: white;">{percentual_tabela_Integral:.2f}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col28:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="color: white;font-size: 14px; font-weight: bold;">DISTRATOS</span>
                         <span style="color: white; font-size: 14px; font-weight: bold;">Assinados + Cancelado: {distrato}</span>
                        <span style="font-size: 14px; color: white;">{formatar_br(distrato_valor)}</span>
                        <span style="font-size: 14px; color: white;">{percentual_distrato_upgrade_sobre_cancelado}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                with col29:
                    st.markdown(
                        f"""
                    <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">TABELA LONGA (60M)</span>
                            <span style="font-size: 20px; color: white;">{tabela_longa}</span>
                            <span style="font-size: 20px; color: white;">{percentual_tabela_longa:.2f}%</span>
                    </div>
                    """,
                        unsafe_allow_html=True
                    )
            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#12172b">
                    <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📊 DESCONTO REAL VIABILIDADE</span>
                        <span style="font-size: 20px; color: white;">R$ {formatar_br(DESCONTO_REAL_VIABILIDADE)}</span>
                        <span style="font-size: 20px; color: white;">{percentual_desconto_real_viabilidade:.2f}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📆 4 SEMANAS</span>
                        <span style="font-size: 20px; color: white;">{tabela_quatro_semanas}</span>
                        <span style="font-size: 20px; color: white;">{percentual_tabela_quatro_semanas:.2f}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col28:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📆 DISTRATOS UPGRADE</span>
                          <span style="color: white; font-size: 14px; font-weight: bold;">Assinados + Cancelado UpGrade: {distrato_upgrade}</span>
                        <span style="font-size: 14px; color: white;">{formatar_br(distrato_valor_up_grade)}</span>
                        <span style="font-size: 14px; color: white;">{percentual_distrato_up_grade}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                with col29:
                    st.markdown(
                        f"""
                    <div class="card" style="background-color:#32CD32">
                            <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">TABELA LONG+ (>60M)</span>
                            <span style="font-size: 20px; color: white;">{tabela_longuissima}</span>
                            <span style="font-size: 20px; color: white;">{percentual_tabela_longuissima:.2f}%</span>
                    </div>
                    """,
                        unsafe_allow_html=True
                    )

            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#fff;">
                    <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📊 GANHO VIABILIDADE</span>
                        <span style="font-size: 20px; color: white;">R$ {formatar_br(total_ganho_viabilidade)}</span>
                        <span style="font-size: 20px; color: white;">{percent_ganho_viabilidade}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📆 6 SEMANAS</span>
                        <span style="font-size: 20px; color: white;">{tabela_seis_semanas}</span>
                        <span style="font-size: 20px; color: white;">{percentual_tabela_seis_semanas:.2f}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col28:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#12172b">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📆 % MÉDIO DE ENTRADA</span>
                        <span style="font-size: 20px; color: white;">{TICKET_MEDIO:.2f}%</span>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#fff;">
                    <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#12172b">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📊 RELATÓRIO COMPLETO</span>
                        <span style="font-size: 20px; color: white;">R$ {formatar_br(valor_final)}</span>
                        <span style="font-size: 20px; color: white;">Total Assinados: {quant_assinado}</span>
                        <span style="font-size: 20px; color: white;">Descontos Aplicados:{formatar_br(total_desconto_financeiro)}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#32CD32">
                        <span style="font-size: 20px; color: white; font-size: 14px; font-weight: bold;">📆 13 SEMANAS</span>
                        <span style="font-size: 20px; color: white;">{tabela_treze_semanas}</span>
                        <span style="font-size: 20px; color: white;">{percentual_tabela_treze_semanas:.2f}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            ####################################################### END HOME #######################################################

            # else:
                # st.write("Nenhum dado encontrado para os filtros selecionados.")


# PÁGINA RANKING
if pagina == 'RANKING':
    st.title('📈 RANKING')
    if not df_filtrado.empty:

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS E 2 LINHAS
        # ============================

        # Criar colunas para os gráficos
        col1, col2 = st.columns(2)

        # ============================
        # 📊 1️⃣ GERENTE: Latência + Produtos
        # ============================
        with col1:
            st.subheader("Ranking de Vendas por GERENTE")
            ranking_gerente = df_filtrado.groupby('GERENTE').agg({
                'Valor vendido': 'sum',
                'PRODUTO': 'count',
                'Latencia de compra': 'mean'
            }).reset_index()

            ranking_gerente.rename(columns={
                'PRODUTO': 'Quantidade de Produtos Vendidos',
                'Latencia de compra': 'Média de Latência (Dias)'
            }, inplace=True)

            ranking_gerente = ranking_gerente.sort_values(
                'Valor vendido', ascending=False)
            st.dataframe(ranking_gerente)

            # Gráfico para GERENTE
            chart = alt.Chart(ranking_gerente).mark_bar().encode(
                x=alt.X('GERENTE:N', title='Gerente'),
                y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
                color=alt.Color('GERENTE:N', title='Gerente'),
                tooltip=[
                    alt.Tooltip('GERENTE:N', title='Gerente'),
                    alt.Tooltip('Valor vendido:Q',
                                title='Valor Vendido', format=',.2f'),
                    alt.Tooltip('Média de Latência (Dias):Q',
                                title='Latência Média', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Vendas por GERENTE'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 📊 2️⃣ CORRETOR 1: Latência + Produtos
        # ============================
        with col2:
            st.subheader("Ranking de Vendas por CORRETOR 1")
            ranking_corretor = df_filtrado.groupby('Corretor 1').agg({
                'Valor vendido': 'sum',
                'PRODUTO': 'count',
                'Latencia de compra': 'mean'
            }).reset_index()

            ranking_corretor.rename(columns={
                'PRODUTO': 'Quantidade de Produtos Vendidos',
                'Latencia de compra': 'Média de Latência (Dias)'
            }, inplace=True)

            ranking_corretor = ranking_corretor.sort_values(
                'Valor vendido', ascending=False)
            st.dataframe(ranking_corretor)

            # Gráfico para CORRETOR 1
            chart = alt.Chart(ranking_corretor).mark_bar().encode(
                x=alt.X('Corretor 1:N', title='Corretor 1'),
                y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
                color=alt.Color('Corretor 1:N', title='Corretor 1'),
                tooltip=[
                    alt.Tooltip('Corretor 1:N', title='Corretor 1'),
                    alt.Tooltip('Valor vendido:Q',
                                title='Valor Vendido', format=',.2f'),
                    alt.Tooltip('Média de Latência (Dias):Q',
                                title='Latência Média', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Vendas por CORRETOR 1'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 🔹 Criar nova linha para os próximos gráficos
        # ============================
        col3, col4 = st.columns(2)

        # ============================
        # 📊 3️⃣ GERENTE com Desconto Financeiro
        # ============================
        with col3:
            st.subheader("GERENTES com Desconto Financeiro")
           # Garantir que as colunas 'Valor vendido' e 'Desconto Financeiro' são numéricas
            df_filtrado['Valor vendido'] = pd.to_numeric(df_filtrado['Valor vendido'], errors='coerce')
            df_filtrado['Desconto Financeiro'] = pd.to_numeric(df_filtrado['Desconto Financeiro'], errors='coerce')

            #Remover valores NaN (caso tenham sido convertidos)
            df_filtrado.fillna(0, inplace=True)

            # Realizar o agrupamento após a conversão correta dos dados
            ranking_gerente_desc = df_filtrado.groupby('GERENTE').agg({
                'Valor vendido': 'sum',
                'Desconto Financeiro': 'sum'
            }).reset_index()

            ranking_melted = ranking_gerente_desc.melt(id_vars='GERENTE',
                                                       value_vars=[
                                                           'Valor vendido', 'Desconto Financeiro'],
                                                       var_name='Tipo',
                                                       value_name='Valor')

            color_scale = alt.Scale(domain=['Valor vendido', 'Desconto Financeiro'],
                                    range=['skyblue', 'red'])

            chart = alt.Chart(ranking_melted).mark_bar().encode(
                x=alt.X('GERENTE:N', title='Gerente', sort='-y'),
                y=alt.Y('Valor:Q', title='Valor Total (R$)'),
                color=alt.Color('Tipo:N', scale=color_scale,
                                title='Tipo de Valor'),
                tooltip=[
                    alt.Tooltip('GERENTE:N', title='Gerente'),
                    alt.Tooltip('Tipo:N', title='Tipo'),
                    alt.Tooltip('Valor:Q', title='Valor (R$)', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Desconto Financeiro por GERENTE'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 📊 4️⃣ CORRETOR 1 com Desconto Financeiro
        # ============================
        with col4:
            st.subheader("CORRETORES com Desconto Financeiro")
            ranking_corretor_desc = df_filtrado.groupby('Corretor 1').agg({
                'Valor vendido': 'sum',
                'Desconto Financeiro': 'sum'
            }).reset_index()

            ranking_melted = ranking_corretor_desc.melt(id_vars='Corretor 1',
                                                        value_vars=[
                                                            'Valor vendido', 'Desconto Financeiro'],
                                                        var_name='Tipo',
                                                        value_name='Valor')

            chart = alt.Chart(ranking_melted).mark_bar().encode(
                x=alt.X('Corretor 1:N', title='Corretor 1', sort='-y'),
                y=alt.Y('Valor:Q', title='Valor Total (R$)'),
                color=alt.Color('Tipo:N', scale=color_scale,
                                title='Tipo de Valor'),
                tooltip=[
                    alt.Tooltip('Corretor 1:N', title='Corretor 1'),
                    alt.Tooltip('Tipo:N', title='Tipo'),
                    alt.Tooltip('Valor:Q', title='Valor (R$)', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Desconto Financeiro por CORRETOR 1'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 🔹 PREPARAÇÃO DOS DADOS
        # ============================

        # Remover espaços extras nos nomes das colunas
        df_filtrado.columns = df_filtrado.columns.str.strip()

        # Converter 'Data da Venda' para datetime e extrair o ano
        df_filtrado['Data da Venda'] = pd.to_datetime(
            df_filtrado['Data da Venda'])
        df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year

        # Verificar se 'Ano' existe e criar se necessário
        if 'Ano' not in df_filtrado.columns:
            df_filtrado['Ano'] = pd.to_datetime(
                df_filtrado['Data da Venda']).dt.year

        # ============================
        # 🔹 INTERFACE DO STREAMLIT
        # ============================

        # Título do app
        st.title("📊 Ranking de Vendas por Gerente por Ano (2022 - 2025)")

        # Filtro de anos disponíveis
        anos_disponiveis = sorted(df_filtrado['Ano'].unique().tolist())
        anos_selecionados = st.multiselect(
            '🔎 Selecione os Anos:', anos_disponiveis, default=anos_disponiveis)

        # Filtrar o DataFrame pelos anos selecionados
        df_filtrado_anos = df_filtrado[df_filtrado['Ano'].isin(
            anos_selecionados)]

        # ============================
        # 🔹 AGRUPAMENTO DE DADOS
        # ============================

        # Agrupar por 'GERENTE' e 'Ano' para somar os valores vendidos
        ranking_gerente_ano = df_filtrado_anos.groupby(
            ['GERENTE', 'Ano'])['Valor vendido'].sum().reset_index()

        # Ordenar por Ano e pelo maior valor vendido
        ranking_gerente_ano = ranking_gerente_ano.sort_values(
            ['Ano', 'Valor vendido'], ascending=[True, False])

        # ============================
        # 🔹 GRÁFICO ALTAIR (Com Layering Correto)
        # ============================

        # Criar gráfico de barras
        bars = alt.Chart(ranking_gerente_ano).mark_bar().encode(
            x=alt.X('GERENTE:N', title='Gerente'),
            y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
            color=alt.Color('GERENTE:N', title='Gerente'),
            tooltip=[
                alt.Tooltip('GERENTE:N', title='Gerente'),
                alt.Tooltip('Ano:N', title='Ano'),
                alt.Tooltip('Valor vendido:Q',
                            title='Valor Vendido', format=',.2f')
            ]
        )

        # Adicionar rótulos de valores nas barras
        text = bars.mark_text(
            align='center',
            baseline='bottom',
            dy=-5,  # Ajuste vertical do texto
            fontSize=10
        ).encode(
            text=alt.Text('Valor vendido:Q', format=',.2f')
        )

        # Layer dos gráficos (barras + rótulos)
        layered_chart = alt.layer(bars, text)

        # Facetear o gráfico por Ano após o layering
        final_chart = layered_chart.facet(
            column=alt.Column('Ano:N', title='Ano')
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        )

        # ============================
        # 🔹 EXIBIÇÃO NO STREAMLIT
        # ============================
        st.altair_chart(final_chart, use_container_width=True)

        # ============================
        # 🔹 TABELA DE DADOS (Opcional)
        # ============================
        st.subheader("📋 Dados de Vendas por Ano e Gerente")
        st.dataframe(ranking_gerente_ano)

    else:
        st.write("Nenhum dado encontrado para o ranking.")

# PÁGINA ORIGENS E ESTADOS
elif pagina == 'Origens_Estados':
    st.title('🌍 Origens e Estados')
    if not df_filtrado.empty:

        # ============================
        # 🔹 Agrupamento com '# Clientes'
        # ============================
        # Agrupar por 'Origem da venda' e 'UF', somar o valor vendido e contar clientes únicos
        origens_estados = df_filtrado.groupby(['Origem da venda', 'UF']).agg({
            'Valor vendido': 'sum',
            'CLIENTE': 'nunique'  # Contar clientes únicos
        }).reset_index()

        # Renomear a coluna para '# Clientes'
        origens_estados.rename(columns={'CLIENTE': '# Clientes'}, inplace=True)

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS E 2 LINHAS
        # ============================

        # Criar as colunas para os gráficos e tabelas
        col1, col2 = st.columns(2)

        # ============================
        # 📊 1️⃣ TABELA: Origens e Estados
        # ============================
        with col1:
            st.subheader("📋 Origens por Estado com # Clientes")
            st.dataframe(origens_estados)

        # ============================
        # 📊 2️⃣ GRÁFICO: Valor Vendido por Origem
        # ============================
        with col2:
            st.subheader("📊 Valor Vendido por Origem da Venda")
            chart = pd.pivot_table(df_filtrado, index='Origem da venda',
                                   values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart, x='Origem da venda', y='Valor vendido')

        # ============================
        # 🔹 NOVA LINHA PARA MAIS GRÁFICOS
        # ============================
        col3, col4 = st.columns(2)

        # ============================
        # 📊 3️⃣ GRÁFICO: Valor Vendido por Estado
        # ============================
        with col3:
            st.subheader("📊 Valor Vendido por UF")
            chart_uf = pd.pivot_table(
                df_filtrado, index='UF', values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart_uf, x='UF', y='Valor vendido')

        # ============================
        # 📊 4️⃣ TABELA: Clientes por Origem
        # ============================
        with col4:
            st.subheader("📋 Número de Clientes por Origem")
            clientes_por_origem = df_filtrado.groupby(
                'Origem da venda')['CLIENTE'].nunique().reset_index()
            clientes_por_origem.rename(
                columns={'CLIENTE': '# Clientes'}, inplace=True)
            st.dataframe(clientes_por_origem)

        # Agrupar por 'Origem da venda' e 'UF', somar o valor vendido e contar o número de clientes
        origens_estados = df_filtrado.groupby(['Origem da venda', 'UF']).agg({
            'Valor vendido': 'sum',
            'CLIENTE': 'nunique'  # Conta o número de clientes únicos
        }).reset_index()

        # Renomear a coluna para '# Clientes'
        origens_estados.rename(columns={'CLIENTE': '# Clientes'}, inplace=True)

        # Exibir a tabela atualizada no Streamlit
        st.write(origens_estados)

        # ============================
        # 🔹 Agrupamento com '# Clientes'
        # ============================
        # Agrupar por 'Campanha' e 'UF', somar o valor vendido e contar clientes únicos
        campanha_estados = df_filtrado.groupby(['Campanha', 'UF']).agg({
            'Valor vendido': 'sum',
            'CLIENTE': 'nunique'  # Contar clientes únicos
        }).reset_index()

        # Renomear a coluna para '# Clientes'
        campanha_estados.rename(
            columns={'CLIENTE': '# Clientes'}, inplace=True)

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS E 2 LINHAS
        # ============================

        # Criar as colunas para os gráficos e tabelas
        col1, col2 = st.columns(2)

        # ============================
        # 📊 1️⃣ TABELA: Campanha e Estados
        # ============================
        with col1:
            st.subheader("📋 Campanhas por Estado com # Clientes")

            # Exemplo de agrupamento por campanha e estado
            campanha_estados = df.groupby(['Campanha', 'UF'])[
                'Valor vendido'].sum().reset_index()

        # Exibe o DataFrame na tela
            st.dataframe(campanha_estados)

            # ============================
            # 📊 2️⃣ GRÁFICO: Valor Vendido por Campanha
            # ============================
        with col2:
            st.subheader("📊 Valor Vendido por Campanha")
            chart_campanha = pd.pivot_table(
                df_filtrado, index='Campanha', values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart_campanha, x='Campanha', y='Valor vendido')

            # ============================
            # 🔹 NOVA LINHA PARA MAIS GRÁFICOS
            # ============================
        col3, col4 = st.columns(2)

        # ============================
        # 📊 3️⃣ GRÁFICO: Valor Vendido por Estado
        # ============================
        with col3:
            st.subheader("📊 Valor Vendido por UF")
            chart_uf = pd.pivot_table(
                df_filtrado, index='UF', values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart_uf, x='UF', y='Valor vendido')

            # ============================
            # 📊 4️⃣ TABELA: Clientes por Campanha
            # ============================
        with col4:
            st.subheader("📋 Número de Clientes por Campanha")
            clientes_por_campanha = df_filtrado.groupby(
                'Campanha')['CLIENTE'].nunique().reset_index()
            clientes_por_campanha.rename(
                columns={'CLIENTE': '# Clientes'}, inplace=True)
            st.dataframe(clientes_por_campanha)

            # Remover espaços extras nos nomes das colunas
            df_filtrado.columns = df_filtrado.columns.str.strip()

            # Converter 'Data da Venda' para datetime e extrair o ano
            df_filtrado['Data da Venda'] = pd.to_datetime(
                df_filtrado['Data da Venda'])
            df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year

            # Verificar se 'Ano' existe e criar se necessário
        if 'Ano' not in df_filtrado.columns:
            df_filtrado['Ano'] = pd.to_datetime(
                df_filtrado['Data da Venda']).dt.year

            # ============================
            # 🔹 INTERFACE DO STREAMLIT
            # ============================

            # Título do app
            st.title("📊 Ranking de Vendas por Campanha por Ano (2022 - 2025)")

            # Filtro de anos disponíveis
            anos_disponiveis = sorted(df_filtrado['Ano'].unique().tolist())
            anos_selecionados = st.multiselect(
                '🔎 Selecione os Anos:', anos_disponiveis, default=anos_disponiveis)

            # Filtrar o DataFrame pelos anos selecionados
            df_filtrado_anos = df_filtrado[df_filtrado['Ano'].isin(
                anos_selecionados)]

            # ============================
            # 🔹 AGRUPAMENTO DE DADOS
            # ============================

            # Agrupar por 'Campanha' e 'Ano' para somar os valores vendidos
            ranking_campanha_ano = df_filtrado_anos.groupby(
                ['Campanha', 'Ano'])['Valor vendido'].sum().reset_index()

            # Ordenar por Ano e pelo maior valor vendido
            ranking_campanha_ano = ranking_campanha_ano.sort_values(
                ['Ano', 'Valor vendido'], ascending=[True, False])

            # ============================
            # 🔹 GRÁFICO ALTAIR (Com Layering Correto)
            # ============================

            # Criar gráfico de barras
            bars = alt.Chart(ranking_campanha_ano).mark_bar().encode(
                x=alt.X('Campanha:N', title='Campanha'),
                y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
                color=alt.Color('Campanha:N', title='Campanha'),
                tooltip=[
                    alt.Tooltip('Campanha:N', title='Campanha'),
                    alt.Tooltip('Ano:N', title='Ano'),
                    alt.Tooltip('Valor vendido:Q',
                                title='Valor Vendido', format=',.2f')
                ]
            )

            # Adicionar rótulos de valores nas barras
            text = bars.mark_text(
                align='center',
                baseline='bottom',
                dy=-5,  # Ajuste vertical do texto
                fontSize=10
            ).encode(
                text=alt.Text('Valor vendido:Q', format=',.2f')
            )

            # Layer dos gráficos (barras + rótulos)
            layered_chart = alt.layer(bars, text)

            # Facetear o gráfico por Ano após o layering
            final_chart = layered_chart.facet(
                column=alt.Column('Ano:N', title='Ano')
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            ).configure_title(
                fontSize=16
            )

            # ============================
            # 🔹 EXIBIÇÃO NO STREAMLIT
            # ============================
            st.altair_chart(final_chart, use_container_width=True)

            # ============================
            # 🔹 TABELA DE DADOS (Opcional)
            # ============================
            st.subheader("📋 Dados de Vendas por Ano e Campanha")
            st.dataframe(ranking_campanha_ano)

        else:
            st.write("Nenhum dado encontrado.")


# PÁGINA GRÁFICOS TABELA
if pagina == 'GRÁFICOS TABELA':
    #st.title('📊 Gráficos Tabela')
    if not df_filtrado.empty:

        
        
        
        
        # ============================
        # 🔹 Simulação de Dados (substitua pelo seu df_filtrado)
        # ============================

        # Converter 'Data da Venda' para datetime e extrair o ano
        df_filtrado['Data da Venda'] = pd.to_datetime(
            df_filtrado['Data da Venda'])
        df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS, 4 LINHAS (1/4 PROPORÇÃO)
        # ============================

        # Título do app
     

       
#############################Inicio Grafico ######################################
        # Linha de separação
        st.markdown("---")
        # Título personalizado com HTML e CSS
        st.markdown("""
        <h1 style='color: blue; font-size: 18px;'>📈 Vendas Mês a Mês - Á Vista (Filtrável por Ano e Tipo de Unidade)</h1>
        """, unsafe_allow_html=True)

 # ============================
        # 📊 1️⃣ LINHA 1: TABELA E GRÁFICO PRINCIPAL
        # _________________________________________________________________________________________#

        df_a_vista = df_filtrado[df_filtrado['Tabela']
                                 == 'A vista']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_a_vista2 = df_a_vista.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_a_vista = round((quant_a_vista / total_registros) * 100)
        percent_a_vista2 = round(
            (quant_a_vista2 / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#
        # ============================
 # ✅ Agrupar por Ano e Mês e somar os valores

 #########################################################################################

    # ============================
    # 🔹 FILTRAR DADOS "À VISTA"
    # ============================

    # ✅ Filtrar apenas vendas "À vista"
        df_a_vista = df[df['Tabela'].str.strip().str.lower() == 'a vista']

    # ✅ Garantir que 'Data da Venda' está em formato datetime
        df_a_vista['Data da Venda'] = pd.to_datetime(
            df_a_vista['Data da Venda'], errors='coerce')
        df_a_vista = df_a_vista.dropna(subset=['Data da Venda'])

    # ✅ Criar colunas para Ano e Mês
        df_a_vista['Ano'] = df_a_vista['Data da Venda'].dt.year
        df_a_vista['Mês'] = df_a_vista['Data da Venda'].dt.month

    # ============================
    # 🔹 FILTRO DE ANO COM `key`
    # ============================

    # ✅ Lista de anos disponíveis
        anos_disponiveis = sorted(df_a_vista['Ano'].unique())
        default_anos = anos_disponiveis if anos_disponiveis else []

    # ✅ Filtro de anos (com `key` para evitar duplicação)
        anos_selecionados = st.multiselect(
            '📅 **Selecione os anos para visualizar:**',
            anos_disponiveis,
            default=default_anos,
            key='filtro_anos_a_vista'  # ✅ Chave única
        )

    # ============================
    # 🔹 FILTRO DE "Tipo unidade semanas" COM `key`
    # ============================

    # Obter os tipos de unidade disponíveis
        tipos_unidade = df_a_vista['Tipo unidade semanas'].dropna(
        ).unique().tolist()
        tipos_unidade.insert(0, 'Todos')  # Adiciona a opção "Todos"

    # ✅ Filtro de Tipo Unidade Semanas (com `key`)
        tipo_unidade_selecionado = st.selectbox(
            '🏡 **Selecione o Tipo de Unidade (semanas):**',
            tipos_unidade,
            key='filtro_tipo_unidade_a_vista'  # ✅ Chave única
        )

    # ============================
    # 🔹 APLICAR FILTROS
    # ============================

    # ✅ Filtrar por ano
        df_filtrado = df_a_vista[df_a_vista['Ano'].isin(anos_selecionados)]

    # ✅ Filtrar por Tipo Unidade Semanas (se não for "Todos")
    if tipo_unidade_selecionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas']
                                  == tipo_unidade_selecionado]

    # ============================
    # 🔹 AGRUPAR DADOS
    # ============================

    # ✅ Agrupar por Ano e Mês e somar os valores vendidos e contar clientes
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'sum'  # ✅ Soma a quantidade de clientes
        }).reset_index()

    # ============================
    # 🔹 GRÁFICO DE LINHAS
    # ============================

        #st.title("📈 Vendas Mês a Mês - À Vista (Filtrável por Ano e Tipo de Unidade)")
        # ✅ Verificar as colunas antes de prosseguir
           #st.write("Colunas disponíveis:", df.columns.tolist())

    # ✅ Extraindo o mês da coluna de data
    df['Mês'] = df['Data da Venda'].dt.month

    # Simulando filtro aplicado
    #df_filtrado = df.copy()

    # ✅ Verificar se 'Mês' foi criado corretamente
    st.write("Amostra dos dados após extração do Mês:")

    # Anos selecionados para o gráfico
    anos_selecionados = [2022, 2023, 2024, 2025]

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Cores e marcadores para os anos
    cores = {2022: 'blue', 2023: 'green', 2024: 'orange', 2025: 'red'}
    marcadores = {2022: 'o', 2023: 's', 2024: '^', 2025: 'D'}

    # Verifica se há dados após o filtro
    if not df_filtrado.empty:
        # ✅ Agrupamento corrigido
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'sum'
        }).reset_index()

        # ✅ Verificar se o agrupamento ocorreu corretamente
        st.write("Vendas agrupadas por Ano e Mês:")

        # Plotar linhas para cada ano selecionado
        for ano in anos_selecionados:
            df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]

            # Verifica se há dados para o ano selecionado
            if not df_ano.empty:
                ax.plot(df_ano['Mês'], df_ano['Valor vendido'],
                        marker=marcadores.get(ano, 'o'),
                        color=cores.get(ano, 'black'),
                        label=str(ano))

                # Adicionar rótulos com quantidade de clientes e valor vendido
                for i, row in df_ano.iterrows():
                    ax.text(row['Mês'], row['Valor vendido'],
                            f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                            ha='center', va='bottom', fontsize=8)

        # Configurações do gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Valor Vendido (R$)')
        ax.set_title('Evolução das Vendas À Vista por Ano e Tipo de Unidade')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul',
                            'Ago', 'Set', 'Out', 'Nov', 'Dez'])
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
        ax.legend(title='Ano')

        # Exibir o gráfico
        st.pyplot(fig)

        # Exibir a tabela de dados
        #st.subheader("📋 Vendas Mensais - À Vista")
        #st.dataframe(df_vendas_agrupadas)

    else:
        st.warning("⚠️ Nenhum dado disponível após o filtro aplicado.")




    #############################Fim Grafico##########################################

    # Linha de separação
    st.markdown("---")
    # Título personalizado com HTML e CSS
    st.markdown("""
    <h1 style='color: blue; font-size: 18px;'>📈 Vendas Mês a Mês - Curta (Filtrável por Ano e Tipo de Unidade)</h1>
    """, unsafe_allow_html=True)

    # ====================
    # 🔹 FILTRAR DADOS "CURTA"
    # ============================

    # ✅ Filtrar apenas vendas "Curta", corrigindo espaços e maiúsculas
    df_vendas_curta = df[df['Tabela'].str.strip().str.lower() == 'curta']

    # ✅ Garantir que 'Data da Venda' está em formato datetime
    df_vendas_curta['Data da Venda'] = pd.to_datetime(
        df_vendas_curta['Data da Venda'], errors='coerce')
    df_vendas_curta = df_vendas_curta.dropna(subset=['Data da Venda'])

    # ✅ Criar colunas para Ano e Mês
    df_vendas_curta['Ano'] = df_vendas_curta['Data da Venda'].dt.year
    df_vendas_curta['Mês'] = df_vendas_curta['Data da Venda'].dt.month

    # ============================
    # 🔹 FILTRO DE ANO
    # ============================

    # Obtenha apenas os anos disponíveis
    anos_disponiveis_curta = sorted(df_vendas_curta['Ano'].unique())
    default_anos_curta = anos_disponiveis_curta if anos_disponiveis_curta else []

    # ✅ Filtro de Ano
    anos_selecionados_curta = st.multiselect(
        '📅 **Selecione os anos para visualizar:**',
        anos_disponiveis_curta,
        default=default_anos_curta
    )

    # ============================
    # 🔹 FILTRO DE "Tipo unidade semanas"
    # ============================

    # Obter os tipos de unidade disponíveis
    tipos_unidade = df_vendas_curta['Tipo unidade semanas'].dropna(
    ).unique().tolist()
    tipos_unidade.insert(0, 'Todos')  # Adiciona a opção "Todos"

    # ✅ Filtro de Tipo Unidade Semanas
    tipo_unidade_selecionado = st.selectbox(
        '🏡 **Selecione o Tipo de Unidade (semanas):**',
        tipos_unidade
    )

    # ============================
    # 🔹 APLICAR FILTROS
    # ============================

    # ✅ Filtrar por ano
    df_vendas_curta_filtrado = df_vendas_curta[df_vendas_curta['Ano'].isin(
        anos_selecionados_curta)]

    # ✅ Filtrar por Tipo Unidade Semanas (se não for "Todos")
    if tipo_unidade_selecionado != 'Todos':
        df_vendas_curta_filtrado = df_vendas_curta_filtrado[
            df_vendas_curta_filtrado['Tipo unidade semanas'] == tipo_unidade_selecionado]

    # ============================
    # 🔹 AGRUPAR E PLOTAR O GRÁFICO
    # ============================

    # ✅ Agrupar por Ano e Mês e somar os valores vendidos e contar clientes
    df_agrupado_curta = df_vendas_curta_filtrado.groupby(['Ano', 'Mês']).agg({
        'Valor vendido': 'sum',
        '# Clientes': 'sum'  # ✅ Soma a quantidade de clientes
    }).reset_index()

    # ============================
    # 🔹 GRÁFICO DE LINHAS
    # ============================

    #st.title("📈 Vendas Mês a Mês - Curta (Filtrável por Ano e Tipo de Unidade)")

    # Criar gráfico
    figura_curta, eixo_curta = plt.subplots(figsize=(12, 6))

    # Cores e marcadores para os anos
    cores_anos = {2022: 'blue', 2023: 'green', 2024: 'orange', 2025: 'red'}
    marcadores_anos = {2022: 'o', 2023: 's', 2024: '^', 2025: 'D'}

    # Verifica se há dados após o filtro
    if not df_vendas_curta_filtrado.empty:
        # Plotar linhas para cada ano selecionado
        for ano_curta in anos_selecionados_curta:
            df_ano_curta = df_agrupado_curta[df_agrupado_curta['Ano'] == ano_curta]
            if not df_ano_curta.empty:
                eixo_curta.plot(df_ano_curta['Mês'], df_ano_curta['Valor vendido'],
                                marker=marcadores_anos.get(ano_curta, 'o'),
                                color=cores_anos.get(ano_curta, 'black'),
                                label=str(ano_curta))

                # Adicionar rótulos de quantidade de clientes
                for i, row in df_ano_curta.iterrows():
                    eixo_curta.text(row['Mês'], row['Valor vendido'],
                                    f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                                    ha='center', va='bottom', fontsize=8)

        # Configurações do gráfico
        eixo_curta.set_xlabel('Mês')
        eixo_curta.set_ylabel('Valor Vendido (R$)')
        eixo_curta.set_title('Evolução das Vendas Curta por Ano e Tipo de Unidade')
        eixo_curta.grid(True, linestyle='--', alpha=0.7)
        eixo_curta.set_xticks(range(1, 13))
        eixo_curta.set_xticklabels(
            ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
        eixo_curta.yaxis.set_major_formatter(
            mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
        eixo_curta.legend(title='Ano')

        # Exibir o gráfico
        st.pyplot(figura_curta)

        # Exibir a tabela de dados
        #st.subheader("📋 Vendas Mensais - Curta")
        #st.dataframe(df_agrupado_curta)
    else:
        st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")


    ######################FIM CURTA######################################
    # Linha de separação
    st.markdown("---")

    # Título personalizado com HTML e CSS
    st.markdown("""
    <h1 style='color: blue; font-size: 18px;'>Vendas Mês a Mês - Longa (Filtrável por Ano e Tipo de Unidade)</h1>
    """, unsafe_allow_html=True)
    # ============================
    # 🔹 FILTRAR DADOS "LONGA"
    # ============================

    # ✅ Filtrar apenas vendas "Longa"
    df_longa = df[df['Tabela'].str.strip().str.lower() == 'longa']

    # ✅ Garantir que 'Data da Venda' está em formato datetime
    df_longa['Data da Venda'] = pd.to_datetime(
        df_longa['Data da Venda'], errors='coerce')
    df_longa = df_longa.dropna(subset=['Data da Venda'])

    # ✅ Criar colunas para Ano e Mês
    df_longa['Ano'] = df_longa['Data da Venda'].dt.year
    df_longa['Mês'] = df_longa['Data da Venda'].dt.month

    # ============================
    # 🔹 FILTRO DE ANO
    # ============================

    # ✅ Lista de anos disponíveis
    anos_disponiveis = sorted(df_longa['Ano'].unique())
    default_anos = anos_disponiveis if anos_disponiveis else []

    # ✅ Filtro de anos (com `key` para evitar duplicação)
    anos_selecionados = st.multiselect(
        '📅 **Selecione os anos para visualizar:**',
        anos_disponiveis,
        default=default_anos,
        key='filtro_anos_longa'  # ✅ Chave única para evitar conflitos
    )

    # ============================
    # 🔹 FILTRO DE "Tipo unidade semanas"
    # ============================

    # Obter os tipos de unidade disponíveis
    tipos_unidade = df_longa['Tipo unidade semanas'].dropna().unique().tolist()
    tipos_unidade.insert(0, 'Todos')  # Adiciona a opção "Todos"

    # ✅ Filtro de Tipo Unidade Semanas
    tipo_unidade_selecionado = st.selectbox(
        '🏡 **Selecione o Tipo de Unidade (semanas):**',
        tipos_unidade,
        key='filtro_tipo_unidade_longa'  # ✅ Chave única
    )

    # ============================
    # 🔹 APLICAR FILTROS
    # ============================

    # ✅ Filtrar por ano
    df_filtrado = df_longa[df_longa['Ano'].isin(anos_selecionados)]

    # ✅ Filtrar por Tipo Unidade Semanas (se não for "Todos")
    if tipo_unidade_selecionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas']
                                == tipo_unidade_selecionado]

    # ============================
    # 🔹 AGRUPAR DADOS
    # ============================

    # ✅ Agrupar por Ano e Mês e somar os valores vendidos e contar clientes
    df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
        'Valor vendido': 'sum',
        '# Clientes': 'sum'  # ✅ Soma a quantidade de clientes
    }).reset_index()

    # ============================
    # 🔹 GRÁFICO DE LINHAS
    # ============================

    #st.title("📈 Vendas Mês a Mês - Longa (Filtrável por Ano e Tipo de Unidade)")

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Cores e marcadores para os anos
    cores = {2022: 'blue', 2023: 'green', 2024: 'orange', 2025: 'red'}
    marcadores = {2022: 'o', 2023: 's', 2024: '^', 2025: 'D'}

    # Verifica se há dados após o filtro
    if not df_filtrado.empty:
        # Plotar linhas para cada ano selecionado
        for ano in anos_selecionados:
            df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]
            if not df_ano.empty:
                ax.plot(df_ano['Mês'], df_ano['Valor vendido'],
                        marker=marcadores.get(ano, 'o'),
                        color=cores.get(ano, 'black'),
                        label=str(ano))

                # Adicionar rótulos com quantidade de clientes e valor vendido
                for i, row in df_ano.iterrows():
                    ax.text(row['Mês'], row['Valor vendido'],
                            f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                            ha='center', va='bottom', fontsize=8)

        # Configurações do gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Valor Vendido (R$)')
        ax.set_title('Evolução das Vendas Longa por Ano e Tipo de Unidade')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai',
                        'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
        ax.yaxis.set_major_formatter(
            mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
        ax.legend(title='Ano')

        # Exibir o gráfico
        st.pyplot(fig)

            # Exibir a tabela de dados
        #st.subheader("📋 Vendas Mensais - Curta")
        #st.dataframe(df_vendas_agrupadas)

    else:
        st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")



    #########################FIM LONGA########################################
    # Linha de separação
    st.markdown("---")
    ##########################INICIO LONGUISSIMA##############################

    # Título personalizado com HTML e CSS
    st.markdown("""
    <h1 style='color: blue; font-size: 18px;'>Vendas Mês a Mês - Longuissima (Filtrável por Ano e Tipo de Unidade)</h1>
    """, unsafe_allow_html=True)
    # ============================
    # 🔹 FILTRAR DADOS "LONGUISSIMA"
    # ============================

    # ✅ Filtrar apenas vendas "Longuissima"
    df_longuissima = df[df['Tabela'].str.strip().str.lower() == 'longuissima']

    # ✅ Garantir que 'Data da Venda' está em formato datetime
    df_longuissima['Data da Venda'] = pd.to_datetime(
        df_longuissima['Data da Venda'], errors='coerce')
    df_longuissima = df_longuissima.dropna(subset=['Data da Venda'])

    # ✅ Criar colunas para Ano e Mês
    df_longuissima['Ano'] = df_longuissima['Data da Venda'].dt.year
    df_longuissima['Mês'] = df_longuissima['Data da Venda'].dt.month

    # ============================
    # 🔹 FILTRO DE ANO
    # ============================

    # ✅ Lista de anos disponíveis
    anos_disponiveis = sorted(df_longuissima['Ano'].unique())
    default_anos = anos_disponiveis if anos_disponiveis else []

    # ✅ Filtro de anos (com `key` para evitar duplicação)
    anos_selecionados = st.multiselect(
        '📅 **Selecione os anos para visualizar:**',
        anos_disponiveis,
        default=default_anos,
        key='filtro_anos_longuissima'  # ✅ Chave única para evitar conflitos
    )

    # ============================
    # 🔹 FILTRO DE "Tipo unidade semanas"
    # ============================




    # Obter os tipos de unidade disponíveis
    tipos_unidade = df_longuissima['Tipo unidade semanas'].dropna(
    ).unique().tolist()
    tipos_unidade.insert(0, 'Todos')  # Adiciona a opção "Todos"

    # ✅ Filtro de Tipo Unidade Semanas
    tipo_unidade_selecionado = st.selectbox(
        '🏡 **Selecione o Tipo de Unidade (semanas):**',
        tipos_unidade,
        key='filtro_tipo_unidade_longuissima'  # ✅ Chave única
    )

    # ============================
    # 🔹 APLICAR FILTROS
    # ============================

    # ✅ Filtrar por ano
    df_filtrado = df_longuissima[df_longuissima['Ano'].isin(anos_selecionados)]

    # ✅ Filtrar por Tipo Unidade Semanas (se não for "Todos")
    if tipo_unidade_selecionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas']
                                == tipo_unidade_selecionado]

    # ============================
    # 🔹 AGRUPAR DADOS
    # ============================

    # ✅ Agrupar por Ano e Mês e somar os valores vendidos e contar clientes
    df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
        'Valor vendido': 'sum',
        '# Clientes': 'sum'  # ✅ Soma a quantidade de clientes
    }).reset_index()

    # ============================
    # 🔹 GRÁFICO DE LINHAS
    # ============================

    #st.title("📈Vendas Mês a Mês - Longuissima (Filtrável por Ano e Tipo de Unidade)")

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Cores e marcadores para os anos
    cores = {2022: 'blue', 2023: 'green', 2024: 'orange', 2025: 'red'}
    marcadores = {2022: 'o', 2023: 's', 2024: '^', 2025: 'D'}

    # Verifica se há dados após o filtro
    if not df_filtrado.empty:
        # Plotar linhas para cada ano selecionado
        for ano in anos_selecionados:
            df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]
            if not df_ano.empty:
                ax.plot(df_ano['Mês'], df_ano['Valor vendido'],
                        marker=marcadores.get(ano, 'o'),
                        color=cores.get(ano, 'black'),
                        label=str(ano))

                # Adicionar rótulos com quantidade de clientes e valor vendido
                for i, row in df_ano.iterrows():
                    ax.text(row['Mês'], row['Valor vendido'],
                            f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                            ha='center', va='bottom', fontsize=8)

        # Configurações do gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Valor Vendido (R$)')
        ax.set_title('Evolução das Vendas Longuissima por Ano e Tipo de Unidade')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai',
                        'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
        ax.yaxis.set_major_formatter(
            mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
        ax.legend(title='Ano')

        # Exibir o gráfico
        st.pyplot(fig)
        # Exibir a tabela de dados
        #st.subheader("📋 Vendas Mensais - Longuissima")
        #st.dataframe(df_vendas_agrupadas)
    else:
        st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")

    

    # Exibir gráfico de clientes por campanha
    #st.subheader("📊 Gráfico de Clientes por Campanha")

#########################################################INICIO SESSAO TABELA##########################################
# PÁGINA GRÁFICOS TABELA
if pagina == 'GRÁFICOS VIABILIDADE':
#st.title('📊 Gráficos Tabela')
    if not df_filtrado.empty:






        

        # ============================
        # 🔹 TÍTULO PERSONALIZADO COM HTML E CSS
        # ============================
        st.markdown("""
            <h1 style='color: blue; font-size: 22px; text-align: center;'>Desconto Financeiro Mês a Mês (Filtrável por Ano e Tipo de Unidade)</h1>
        """, unsafe_allow_html=True)

        # ============================
        # 🔹 FILTRAR DADOS
        # ============================
        df_vendas = df.copy()

        # ✅ Converter 'Data da Venda' para datetime
        df_vendas['Data da Venda'] = pd.to_datetime(df_vendas['Data da Venda'], errors='coerce')
        df_vendas.dropna(subset=['Data da Venda'], inplace=True)

        # ✅ Criar colunas de Ano e Mês
        df_vendas['Ano'] = df_vendas['Data da Venda'].dt.year
        df_vendas['Mês'] = df_vendas['Data da Venda'].dt.month

        # ✅ Converter colunas numéricas para float para evitar erro no groupby
        colunas_numericas = ['Valor vendido', 'Desconto Financeiro', '# Clientes']
        for coluna in colunas_numericas:
            df_vendas[coluna] = pd.to_numeric(df_vendas[coluna], errors='coerce').fillna(0)

        # ============================
        # 🔹 FILTROS
        # ============================

        # ✅ Filtro de Ano
        anos_disponiveis = sorted(df_vendas['Ano'].unique())
        anos_selecionados = st.multiselect('📅 **Selecione os anos:**', anos_disponiveis, default=anos_disponiveis)

        # ✅ Filtro de Tipo Unidade Semanas
        tipos_unidade = ['Todos'] + df_vendas['Tipo unidade semanas'].dropna().unique().tolist()
        tipo_unidade_selecionado = st.selectbox('🏡 **Selecione o Tipo de Unidade:**', tipos_unidade)

        # ✅ Aplicação dos filtros
        df_filtrado = df_vendas[df_vendas['Ano'].isin(anos_selecionados)]
        if tipo_unidade_selecionado != 'Todos':
            df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas'] == tipo_unidade_selecionado]

        # ============================
        # 🔹 AGRUPAMENTO DOS DADOS
        # ============================
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            'Desconto Financeiro': 'sum',  # ✅ Soma do Desconto Financeiro
            '# Clientes': 'sum'
        }).reset_index()

        # ============================
        # 🔹 OPÇÃO PARA LIGAR/DESLIGAR "VALOR VENDIDO"
        # ============================
        exibir_valor_vendido = st.checkbox("🔄 Mostrar 'Valor Vendido'", value=False)

        # ============================
        # 🔹 GRÁFICO DE LINHAS (Valor Vendido e Desconto Financeiro)
        # ============================
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # 🔹 Gerar cores automaticamente
        cmap = plt.cm.get_cmap('tab10', len(anos_selecionados))
        cores_ano = {ano: cmap(i) for i, ano in enumerate(anos_selecionados)}

        # Criar um segundo eixo y para os descontos financeiros
        ax2 = ax1.twinx()

        # Verifica se há dados
        if not df_vendas_agrupadas.empty:
            for ano in anos_selecionados:
                df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]
                if not df_ano.empty:
                    # 🔹 Plotar Valor Vendido (se estiver ativado no checkbox)
                    if exibir_valor_vendido:
                        ax1.plot(df_ano['Mês'], df_ano['Valor vendido'], marker='o', 
                                color=cores_ano.get(ano, 'black'), label=f'Valor Vendido {ano}')

                    # 🔹 Plotar Desconto Financeiro
                    ax2.plot(df_ano['Mês'], df_ano['Desconto Financeiro'], marker='s', 
                            linestyle='dashed', color=cores_ano.get(ano, 'black'), 
                            alpha=0.6, label=f'Desconto Financeiro {ano}')

                    # 🔹 Adicionar rótulos
                    for i, row in df_ano.iterrows():
                        if exibir_valor_vendido:
                            ax1.text(row['Mês'], row['Valor vendido'],
                                    f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                                    ha='center', va='bottom', fontsize=8, 
                                    bbox=dict(facecolor='white', alpha=0.7))

                        ax2.text(row['Mês'], row['Desconto Financeiro'],
                                f"-R$ {row['Desconto Financeiro']:,.0f}",
                                ha='center', va='top', fontsize=8, 
                                bbox=dict(facecolor='white', alpha=0.7))

            # Configuração do primeiro eixo (Valor Vendido)
            ax1.set_xlabel('Mês')
            ax1.set_ylabel('Valor Vendido (R$)', color='blue')
            ax1.set_title('Evolução das Vendas e Descontos Financeiros')
            ax1.grid(True, linestyle='--', alpha=0.7)
            ax1.set_xticks(range(1, 13))
            ax1.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
            ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

            # Configuração do segundo eixo (Desconto Financeiro)
            ax2.set_ylabel('Desconto Financeiro (R$)', color='red')
            ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'-R$ {x:,.0f}'))

            # Adicionar legendas separadas para os dois eixos
            if exibir_valor_vendido:
            # 🔹 **Mudar posição da legenda para a parte inferior do gráfico**
                ax1.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=10, ncol=2)
            ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fontsize=10, ncol=2)

            # Exibir gráfico
            st.pyplot(fig)

            # Exibir tabela com os dados agregados
            st.subheader("📋 Vendas Mensais")
            st.dataframe(df_vendas_agrupadas)
        else:
            st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")



    #else:
        #st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")

########################################################FIM SESSA TABELA#################################################




   

        # ============================
        # 🔹 TÍTULO PERSONALIZADO COM HTML E CSS
        # ============================
        st.markdown("""
            <h1 style='color: blue; font-size: 22px; text-align: center;'>Desconto Real Viabilidade Mês a Mês (Filtrável por Ano e Tipo de Unidade)</h1>
        """, unsafe_allow_html=True)

        # ============================
        # 🔹 FILTRAR DADOS
        # ============================
        df_vendas = df.copy()

        # ✅ Converter 'Data da Venda' para datetime
        df_vendas['Data da Venda'] = pd.to_datetime(df_vendas['Data da Venda'], errors='coerce')
        df_vendas.dropna(subset=['Data da Venda'], inplace=True)

        # ✅ Criar colunas de Ano e Mês
        df_vendas['Ano'] = df_vendas['Data da Venda'].dt.year
        df_vendas['Mês'] = df_vendas['Data da Venda'].dt.month

        # ✅ Converter colunas numéricas para float para evitar erro no groupby
        colunas_numericas = ['Valor vendido', 'Desconto Real Viabilidade', '# Clientes']
        df_vendas[colunas_numericas] = df_vendas[colunas_numericas].apply(pd.to_numeric, errors='coerce').fillna(0)

        # ============================
        # 🔹 FILTROS (Corrigidos com `key`)
        # ============================

        # ✅ Filtro de Ano (corrigido com `key`)
        anos_disponiveis = sorted(df_vendas['Ano'].unique())
        anos_selecionados = st.multiselect('📅 **Selecione os anos:**', anos_disponiveis, default=anos_disponiveis, key="filtro_anos_viabilidade")

        # ✅ Filtro de Tipo Unidade Semanas (corrigido com `key`)
        tipos_unidade = ['Todos'] + df_vendas['Tipo unidade semanas'].dropna().unique().tolist()
        tipo_unidade_selecionado = st.selectbox('🏡 **Selecione o Tipo de Unidade:**', tipos_unidade, key="filtro_tipo_unidade_viabilidade")

        # ✅ Aplicação dos filtros
        df_filtrado = df_vendas[df_vendas['Ano'].isin(anos_selecionados)]
        if tipo_unidade_selecionado != 'Todos':
            df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas'] == tipo_unidade_selecionado]

        # ============================
        # 🔹 AGRUPAMENTO DOS DADOS
        # ============================
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            'Desconto Real Viabilidade': 'sum',  # ✅ Soma do Desconto Real Viabilidade
            '# Clientes': 'sum'
        }).reset_index()

        # ============================
        # 🔹 OPÇÃO PARA LIGAR/DESLIGAR "VALOR VENDIDO" (Corrigido com `key`)
        # ============================
        exibir_valor_vendido = st.checkbox("🔄 Mostrar 'Valor Vendido'", value=True, key="checkbox_valor_vendido_viabilidade")

        # ============================
        # 🔹 GRÁFICO DE LINHAS (Valor Vendido e Desconto Real Viabilidade)
        # ============================
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # 🔹 Gerar cores automaticamente
        cmap = plt.cm.get_cmap('tab10', len(anos_selecionados))
        cores_ano = {ano: cmap(i) for i, ano in enumerate(anos_selecionados)}

        # Criar um segundo eixo y para os descontos financeiros
        ax2 = ax1.twinx()

        # Verifica se há dados
        if not df_vendas_agrupadas.empty:
            for ano in anos_selecionados:
                df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]
                if not df_ano.empty:
                    # 🔹 Plotar Valor Vendido (se estiver ativado no checkbox)
                    if exibir_valor_vendido:
                        ax1.plot(df_ano['Mês'], df_ano['Valor vendido'], marker='o', 
                                color=cores_ano.get(ano, 'black'), label=f'Valor Vendido {ano}')

                    # 🔹 Plotar Desconto Real Viabilidade
                    ax2.plot(df_ano['Mês'], df_ano['Desconto Real Viabilidade'], marker='s', 
                            linestyle='dashed', color=cores_ano.get(ano, 'black'), 
                            alpha=0.6, label=f'Desconto Real Viabilidade {ano}')

                    # 🔹 Adicionar valores sobre os pontos no gráfico
                    for i, row in df_ano.iterrows():
                        if exibir_valor_vendido:
                            ax1.text(row['Mês'], row['Valor vendido'],
                                    f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                                    ha='center', va='bottom', fontsize=8, 
                                    bbox=dict(facecolor='white', alpha=0.7))

                        ax2.text(row['Mês'], row['Desconto Real Viabilidade'],
                                f"-R$ {row['Desconto Real Viabilidade']:,.0f}",
                                ha='center', va='top', fontsize=8, 
                                bbox=dict(facecolor='white', alpha=0.7))

            # Configuração do primeiro eixo (Valor Vendido)
            ax1.set_xlabel('Mês')
            ax1.set_ylabel('Valor Vendido (R$)', color='blue')
            ax1.set_title('📊 Evolução das Vendas e Descontos Real Viabilidade')
            ax1.grid(True, linestyle='--', alpha=0.7)
            ax1.set_xticks(range(1, 13))
            ax1.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])

            # Configuração do segundo eixo (Desconto Real Viabilidade)
            ax2.set_ylabel('Desconto Real Viabilidade (R$)', color='red')
            ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'-R$ {x:,.0f}'))

            # 🔹 **Mudar posição da legenda para a parte inferior do gráfico**
            ax1.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=10, ncol=2)
            ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fontsize=10, ncol=2)

            # Exibir gráfico
            st.pyplot(fig)

            # Exibir tabela com os dados agregados
            st.subheader("📋 Vendas Mensais")
            st.dataframe(df_vendas_agrupadas)

        else:
            st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")


#####################################FIM GRAFICO DESCONTO REAL VIABILIDADE#####################################



        # ============================
        # 🔹 TÍTULO PERSONALIZADO COM HTML E CSS
        # ============================
        st.markdown("""
            <h1 style='color: blue; font-size: 22px; text-align: center;'>Ganho ViabilidadeMês a Mês (Filtrável por Ano e Tipo de Unidade)</h1>
        """, unsafe_allow_html=True)

        # ============================
        # 🔹 FILTRAR DADOS
        # ============================
        df_vendas = df.copy()

        # ✅ Converter 'Data da Venda' para datetime
        df_vendas['Data da Venda'] = pd.to_datetime(df_vendas['Data da Venda'], errors='coerce')
        df_vendas.dropna(subset=['Data da Venda'], inplace=True)

        # ✅ Criar colunas de Ano e Mês
        df_vendas['Ano'] = df_vendas['Data da Venda'].dt.year
        df_vendas['Mês'] = df_vendas['Data da Venda'].dt.month

        # ✅ Converter colunas numéricas para float para evitar erro no groupby
        colunas_numericas = ['Valor vendido', 'Ganho Viabilidade', '# Clientes']
        df_vendas[colunas_numericas] = df_vendas[colunas_numericas].apply(pd.to_numeric, errors='coerce').fillna(0)

        # ============================
        # 🔹 FILTROS (Corrigidos com `key`)
        # ============================

        # ✅ Filtro de Ano (corrigido com `key`)
        anos_disponiveis = sorted(df_vendas['Ano'].unique())
        anos_selecionados = st.multiselect('📅 **Selecione os anos:**', anos_disponiveis, default=anos_disponiveis, key="filtro_anos_ganho_viabilidade")

        # ✅ Filtro de Tipo Unidade Semanas (corrigido com `key`)
        tipos_unidade = ['Todos'] + df_vendas['Tipo unidade semanas'].dropna().unique().tolist()
        tipo_unidade_selecionado = st.selectbox('🏡 **Selecione o Tipo de Unidade:**', tipos_unidade, key="filtro_tipo_unidade_ganho_viabilidade")

        # ✅ Aplicação dos filtros
        df_filtrado = df_vendas[df_vendas['Ano'].isin(anos_selecionados)]
        if tipo_unidade_selecionado != 'Todos':
            df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas'] == tipo_unidade_selecionado]

        # ============================
        # 🔹 AGRUPAMENTO DOS DADOS
        # ============================
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            'Ganho Viabilidade': 'sum',  # ✅ Soma do Ganho Viabilidade
            '# Clientes': 'sum'
        }).reset_index()

        # ============================
        # 🔹 OPÇÃO PARA LIGAR/DESLIGAR "VALOR VENDIDO" (Corrigido com `key`)
        # ============================
        exibir_valor_vendido = st.checkbox("🔄 Mostrar 'Valor Vendido'", value=True, key="checkbox_valor_vendido_ganho_viabilidade")

        # ============================
        # 🔹 GRÁFICO DE LINHAS (Valor Vendido e Ganho Viabilidade)
        # ============================
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # 🔹 Gerar cores automaticamente
        cmap = plt.cm.get_cmap('tab10', len(anos_selecionados))
        cores_ano = {ano: cmap(i) for i, ano in enumerate(anos_selecionados)}

        # Criar um segundo eixo y para os ganhos de viabilidade
        ax2 = ax1.twinx()

        # Verifica se há dados
        if not df_vendas_agrupadas.empty:
            for ano in anos_selecionados:
                df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]
                if not df_ano.empty:
                    # 🔹 Plotar Valor Vendido (se estiver ativado no checkbox)
                    if exibir_valor_vendido:
                        ax1.plot(df_ano['Mês'], df_ano['Valor vendido'], marker='o', 
                                color=cores_ano.get(ano, 'black'), label=f'Valor Vendido {ano}')

                    # 🔹 Plotar Ganho Viabilidade
                    ax2.plot(df_ano['Mês'], df_ano['Ganho Viabilidade'], marker='s', 
                            linestyle='dashed', color=cores_ano.get(ano, 'black'), 
                            alpha=0.6, label=f'Ganho Viabilidade{ano}')

                    # 🔹 Adicionar valores sobre os pontos no gráfico
                    for i, row in df_ano.iterrows():
                        if exibir_valor_vendido:
                            ax1.text(row['Mês'], row['Valor vendido'],
                                    f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                                    ha='center', va='bottom', fontsize=8, 
                                    bbox=dict(facecolor='white', alpha=0.7))

                        ax2.text(row['Mês'], row['Ganho Viabilidade'],
                                f"R$ {row['Ganho Viabilidade']:,.0f}",
                                ha='center', va='top', fontsize=8, 
                                bbox=dict(facecolor='white', alpha=0.7))

            # Configuração do primeiro eixo (Valor Vendido)
            ax1.set_xlabel('Mês')
            ax1.set_ylabel('Valor Vendido (R$)', color='blue')
            ax1.set_title('📊 Evolução das Vendas e Ganho Viabilidade')
            ax1.grid(True, linestyle='--', alpha=0.7)
            ax1.set_xticks(range(1, 13))
            ax1.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])

            # Configuração do segundo eixo (Ganho Viabilidade)
            ax2.set_ylabel('Ganho Viabilidade(R$)', color='green')
            ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

            # 🔹 **Mudar posição da legenda para a parte inferior do gráfico**
            ax1.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=10, ncol=2)
            ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fontsize=10, ncol=2)

            # Exibir gráfico
            st.pyplot(fig)

            # Exibir tabela com os dados agregados
            st.subheader("📋 Vendas Mensais")
            st.dataframe(df_vendas_agrupadas)

        else:
            st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")




#################################################FIM GRAFICO GANHO VIABILIDADE####################################

        import streamlit as st
        import pandas as pd
        import matplotlib.pyplot as plt
        import matplotlib.ticker as mticker

        # ============================
        # 🔹 TÍTULO PERSONALIZADO COM HTML E CSS
        # ============================
        st.markdown("""
            <h1 style='color: blue; font-size: 22px; text-align: center;'>Ganho ViabilidadeMês a Mês (Filtrável por Ano e Tipo de Unidade)</h1>
        """, unsafe_allow_html=True)

        # ============================
        # 🔹 FILTRAR DADOS
        # ============================
        df_vendas = df.copy()

        # ✅ Converter 'Data da Venda' para datetime
        df_vendas['Data da Venda'] = pd.to_datetime(df_vendas['Data da Venda'], errors='coerce')
        df_vendas.dropna(subset=['Data da Venda'], inplace=True)

        # ✅ Criar colunas de Ano e Mês
        df_vendas['Ano'] = df_vendas['Data da Venda'].dt.year
        df_vendas['Mês'] = df_vendas['Data da Venda'].dt.month

        # ✅ Converter colunas numéricas para float para evitar erro no groupby
        colunas_numericas = ['Valor vendido', 'Ganho Viabilidade', '# Clientes']
        df_vendas[colunas_numericas] = df_vendas[colunas_numericas].apply(pd.to_numeric, errors='coerce').fillna(0)

        # ============================
        # 🔹 FILTROS (Corrigidos com `key` único)
        # ============================

        # ✅ Filtro de Ano (corrigido com `key` único)
        anos_disponiveis = sorted(df_vendas['Ano'].unique())
        anos_selecionados = st.multiselect('📅 **Selecione os anos:**', anos_disponiveis, default=anos_disponiveis, key="filtro_anos_ganho_viabilidade_unico")

        # ✅ Filtro de Tipo Unidade Semanas (corrigido com `key` único)
        tipos_unidade = ['Todos'] + df_vendas['Tipo unidade semanas'].dropna().unique().tolist()
        tipo_unidade_selecionado = st.selectbox('🏡 **Selecione o Tipo de Unidade:**', tipos_unidade, key="filtro_tipo_unidade_ganho_viabilidade_unico")

        # ✅ Aplicação dos filtros
        df_filtrado = df_vendas[df_vendas['Ano'].isin(anos_selecionados)]
        if tipo_unidade_selecionado != 'Todos':
            df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas'] == tipo_unidade_selecionado]

        # ============================
        # 🔹 AGRUPAMENTO DOS DADOS
        # ============================
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            'Ganho Viabilidade': 'sum',  # ✅ Soma do Ganho Viabilidade
            '# Clientes': 'sum'
        }).reset_index()

        # ============================
        # 🔹 OPÇÃO PARA LIGAR/DESLIGAR "VALOR VENDIDO" (Corrigido com `key` único)
        # ============================
        exibir_valor_vendido = st.checkbox("🔄 Mostrar 'Valor Vendido'", value=True, key="checkbox_valor_vendido_ganho_viabilidade_unico")

        # ============================
        # 🔹 GRÁFICO DE LINHAS (Valor Vendido e Ganho Viabilidade)
        # ============================
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # 🔹 Gerar cores automaticamente
        cmap = plt.cm.get_cmap('tab10', len(anos_selecionados))
        cores_ano = {ano: cmap(i) for i, ano in enumerate(anos_selecionados)}

        # Criar um segundo eixo y para os ganhos de viabilidade
        ax2 = ax1.twinx()

        # Verifica se há dados
        if not df_vendas_agrupadas.empty:
            for ano in anos_selecionados:
                df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]
                if not df_ano.empty:
                    # 🔹 Plotar Valor Vendido (se estiver ativado no checkbox)
                    if exibir_valor_vendido:
                        ax1.plot(df_ano['Mês'], df_ano['Valor vendido'], marker='o', 
                                color=cores_ano.get(ano, 'black'), label=f'Valor Vendido {ano}')

                    # 🔹 Plotar Ganho Viabilidade
                    ax2.plot(df_ano['Mês'], df_ano['Ganho Viabilidade'], marker='s', 
                            linestyle='dashed', color=cores_ano.get(ano, 'black'), 
                            alpha=0.6, label=f'Ganho Viabilidade{ano}')

                    # 🔹 Adicionar valores sobre os pontos no gráfico
                    for i, row in df_ano.iterrows():
                        if exibir_valor_vendido:
                            ax1.text(row['Mês'], row['Valor vendido'],
                                    f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                                    ha='center', va='bottom', fontsize=8, 
                                    bbox=dict(facecolor='white', alpha=0.7))

                        ax2.text(row['Mês'], row['Ganho Viabilidade'],
                                f"R$ {row['Ganho Viabilidade']:,.0f}",
                                ha='center', va='top', fontsize=8, 
                                bbox=dict(facecolor='white', alpha=0.7))

            # Configuração do primeiro eixo (Valor Vendido)
            ax1.set_xlabel('Mês')
            ax1.set_ylabel('Valor Vendido (R$)', color='blue')
            ax1.set_title('📊 Evolução das Vendas e Ganho Viabilidade')
            ax1.grid(True, linestyle='--', alpha=0.7)
            ax1.set_xticks(range(1, 13))
            ax1.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])

            # Configuração do segundo eixo (Ganho Viabilidade)
            ax2.set_ylabel('Ganho Viabilidade(R$)', color='green')
            ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

            # 🔹 **Mudar posição da legenda para a parte inferior do gráfico**
            ax1.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=10, ncol=2)
            ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fontsize=10, ncol=2)

            # Exibir gráfico
            st.pyplot(fig)

            # Exibir tabela com os dados agregados
            st.subheader("📋 Vendas Mensais")
            st.dataframe(df_vendas_agrupadas)

        else:
            st.warning("⚠️ Nenhum dado disponível para os filtros aplicados.")



# PÁGINA GRÁFICOS DISTRATOS
if pagina == 'GRÁFICOS DISTRATOS':
    st.title('📈 GRÁFICOS DISTRATOS')
    if not df_filtrado.empty:

        ###############################DISTRATOS GRAFICO INICIO##################################################





        #########################Distratios UpGrades########################################
        # Linha de separação
        st.markdown("---")
        # Título personalizado com HTML e CSS
        st.markdown("""
        <h1 style='color: blue; font-size: 18px;'>DISTRATOS Mês a Mês</h1>
        """, unsafe_allow_html=True)


       



       # Converter "Data da Venda" para datetime se ainda não estiver
        df_filtrado["Data da Venda"] = pd.to_datetime(df_filtrado["Data da Venda"], errors='coerce')

        # Criar colunas de Ano e Mês
        df_filtrado["Ano"] = df_filtrado["Data da Venda"].dt.year
        df_filtrado["Mês"] = df_filtrado["Data da Venda"].dt.month

        # Criar lista de anos disponíveis no DataFrame
        anos_disponiveis = sorted(df_filtrado["Ano"].dropna().unique())

        # Criar um seletor no Streamlit para os anos (se aplicável)
        anos_selecionados = st.multiselect(
            "📅 **Selecione os anos para visualizar:**",
            anos_disponiveis,
            default=anos_disponiveis  # Seleciona todos por padrão
        )

        # Criar botão para exibir ou ocultar "Valor vendido"
        mostrar_valor_vendido = st.checkbox("Mostrar Valor Vendido", value=True)

        # Aplicar filtro de anos no DataFrame
        df_filtrado = df_filtrado[df_filtrado["Ano"].isin(anos_selecionados)]

        # Filtrar os registros onde "Status 1" é "ASSINADO" e "Status 2" é "CANCELADO"
        df_distrato = df_filtrado[(df_filtrado["Status 1"] == "ASSINADO") & (df_filtrado["Status 2"] == "CANCELADO")]

        # Somar os valores da coluna "Valor vendido" para esses registros
        distrato_valor = df_distrato["Valor vendido"].sum()
        
        # Contar a quantidade de distratos
        distrato_quantidade = df_distrato.shape[0]

        # Agrupar vendas "À Vista"
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'sum'  # Mantendo apenas as colunas existentes
        }).reset_index()

        # Agrupar distratos
        df_distrato_agrupado = df_distrato.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'count'
        }).reset_index()

        # Criar gráfico interativo com Plotly
        fig = px.line(
            df_vendas_agrupadas if mostrar_valor_vendido else df_distrato_agrupado,
            x='Mês',
            y='Valor vendido',
            color='Ano',
            markers=True,
            title='Evolução das Vendas e Distratos por Ano'
        )

        # Adicionar linha de distratos
        fig.add_scatter(
            x=df_distrato_agrupado['Mês'],
            y=df_distrato_agrupado['Valor vendido'],
            mode='lines+markers',
            name='Distratos',
            line=dict(dash='dash', color='red')
        )

        # Adicionar anotações para quantidade de vendas e valor vendido se "Mostrar Valor Vendido" estiver ativado
        if mostrar_valor_vendido:
            for i, row in df_vendas_agrupadas.iterrows():
                fig.add_annotation(
                    x=row['Mês'],
                    y=row['Valor vendido'],
                    text=f"{int(row['# Clientes'])} vendas\nR$ {row['Valor vendido']:,.0f}",
                    showarrow=True,
                    arrowhead=2,
                    font=dict(color='blue')
                )

        # Adicionar anotações para distratos se "Mostrar Valor Vendido" estiver ativado
        if mostrar_valor_vendido:
            for i, row in df_distrato_agrupado.iterrows():
                fig.add_annotation(
                    x=row['Mês'],
                    y=row['Valor vendido'],
                    text=f"🔴 {int(row['# Clientes'])} distratos\nR$ {row['Valor vendido']:,.0f}",
                    showarrow=True,
                    arrowhead=2,
                    font=dict(color='red')
                )

        # Ajustar layout para zoom
        fig.update_layout(
            xaxis_title='Mês',
            yaxis_title='Valor Vendido (R$)',
            xaxis=dict(tickmode='array', tickvals=list(range(1, 13)), ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']),
            yaxis=dict(tickprefix='R$ ', tickformat=',.0f'),
            hovermode='x unified'
        )

        # Exibir gráfico interativo no Streamlit
        st.plotly_chart(fig, use_container_width=True)

        # Exibir valores de distrato
        st.markdown(f"### 🔴 Valor Total de Distratos: R$ {distrato_valor:,.2f}")
        st.markdown(f"### 🔴 Quantidade Total de Distratos: {distrato_quantidade}")


 ###############################DISTRATOS GRAFICO INICIO##################################################




        #########################Distratios UpGrades########################################
        # Linha de separação
        st.markdown("---")
        # Título personalizado com HTML e CSS
        st.markdown("""
        <h1 style='color: blue; font-size: 18px;'>DISTRATOS UPGRADES Mês a Mês</h1>
        """, unsafe_allow_html=True)


       



       # Converter "Data da Venda" para datetime se ainda não estiver
        df_filtrado["Data da Venda"] = pd.to_datetime(df_filtrado["Data da Venda"], errors='coerce')

        # Criar colunas de Ano e Mês
        df_filtrado["Ano"] = df_filtrado["Data da Venda"].dt.year
        df_filtrado["Mês"] = df_filtrado["Data da Venda"].dt.month

        # Criar lista de anos disponíveis no DataFrame
        anos_disponiveis = sorted(df_filtrado["Ano"].dropna().unique())

        # Criar um seletor no Streamlit para os anos (se aplicável)
        anos_selecionados = st.multiselect(
            "📅 **Selecione os anos para visualizar:**",
            anos_disponiveis,
            default=anos_disponiveis,  # Seleciona todos por padrão
            key="anos_selecionados"
        )

        # Criar botão para exibir ou ocultar "Valor vendido"
        mostrar_valor_vendido = st.checkbox("Mostrar Valor Vendido", value=True, key="mostrar_valor_vendido")

        # Aplicar filtro de anos no DataFrame
        df_filtrado = df_filtrado[df_filtrado["Ano"].isin(anos_selecionados)]

        # Filtrar os registros onde "Status 1" é "ASSINADO" e "Status 2" é "CANCELADO UPGRADE"
        df_distrato = df_filtrado[(df_filtrado["Status 1"] == "ASSINADO") & (df_filtrado["Status 2"] == "CANCELADO UPGRADE")]

        # Somar os valores da coluna "Valor vendido" para esses registros
        distrato_valor = df_distrato["Valor vendido"].sum()
        
        # Contar a quantidade de distratos
        distrato_quantidade = df_distrato.shape[0]

        # Agrupar vendas "À Vista"
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'sum'  # Mantendo apenas as colunas existentes
        }).reset_index()

        # Agrupar distratos
        df_distrato_agrupado = df_distrato.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'count'
        }).reset_index()

        # Criar gráfico interativo com Plotly
        fig = px.line(
            df_vendas_agrupadas if mostrar_valor_vendido else df_distrato_agrupado,
            x='Mês',
            y='Valor vendido',
            color='Ano',
            markers=True,
            title='Evolução das Vendas e Distratos Upgrades por Ano'
        )

        # Adicionar linha de distratos
        fig.add_scatter(
            x=df_distrato_agrupado['Mês'],
            y=df_distrato_agrupado['Valor vendido'],
            mode='lines+markers',
            name='Distratos Upgrades',
            line=dict(dash='dash', color='red')
        )

        # Adicionar anotações para quantidade de vendas e valor vendido se "Mostrar Valor Vendido" estiver ativado
        if mostrar_valor_vendido:
            for i, row in df_vendas_agrupadas.iterrows():
                fig.add_annotation(
                    x=row['Mês'],
                    y=row['Valor vendido'],
                    text=f"{int(row['# Clientes'])} vendas\nR$ {row['Valor vendido']:,.0f}",
                    showarrow=True,
                    arrowhead=2,
                    font=dict(color='blue')
                )

            for i, row in df_distrato_agrupado.iterrows():
                fig.add_annotation(
                    x=row['Mês'],
                    y=row['Valor vendido'],
                    text=f"🔴 {int(row['# Clientes'])} distratos\nR$ {row['Valor vendido']:,.0f}",
                    showarrow=True,
                    arrowhead=2,
                    font=dict(color='red')
                )

        # Ajustar layout para zoom
        fig.update_layout(
            xaxis_title='Mês',
            yaxis_title='Valor Vendido (R$)',
            xaxis=dict(tickmode='array', tickvals=list(range(1, 13)), ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']),
            yaxis=dict(tickprefix='R$ ', tickformat=',.0f'),
            hovermode='x unified'
        )

        # Exibir gráfico interativo no Streamlit
        st.plotly_chart(fig, use_container_width=True)

        # Exibir valores de distrato
        st.markdown(f"### 🔴 Valor Total de Distratos Upgrades: R$ {distrato_valor:,.2f}")
        st.markdown(f"### 🔴 Quantidade Total de Distratos Upgrades: {distrato_quantidade}")




#######################################Graficos Distratos Totais################################



        import streamlit as st
        import pandas as pd
        import plotly.express as px
        import setuptools
        import re

        # Linha de separação
        st.markdown("---")

        # Título personalizado com HTML e CSS
        st.markdown("""
        <h1 style='color: blue; font-size: 18px;'>DISTRATOS Mês a Mês</h1>
        """, unsafe_allow_html=True)

        # Converter "Data da Venda" para datetime se ainda não estiver
        df_filtrado["Data da Venda"] = pd.to_datetime(df_filtrado["Data da Venda"], errors='coerce')

        # Verificar e converter "Data do cancelamento"
        if "Data do cancelamento" in df_filtrado.columns:
            df_filtrado["Data do cancelamento"] = pd.to_datetime(df_filtrado["Data do cancelamento"], errors='coerce')
        else:
            df_filtrado["Data do cancelamento"] = pd.NaT

        # Criar colunas de Ano e Mês para cancelamento
        df_filtrado["Ano Cancelamento"] = df_filtrado["Data do cancelamento"].dt.year
        df_filtrado["Mês Cancelamento"] = df_filtrado["Data do cancelamento"].dt.month

        # Criar lista de anos disponíveis no DataFrame
        anos_disponiveis = sorted(df_filtrado["Ano Cancelamento"].dropna().unique())

        # Criar um seletor no Streamlit para os anos (se aplicável)
        anos_selecionados = st.multiselect(
            "📅 **Selecione os anos para visualizar:**",
            anos_disponiveis,
            default=anos_disponiveis,
            key="anos_selecionados_2"
        )

        # Criar botão para exibir ou ocultar "Valor vendido"
        mostrar_valor_vendido = st.checkbox("Mostrar Valor Vendido", value=True, key="mostrar_valor_vendido_2")

        # Aplicar filtro de anos no DataFrame
        df_filtrado = df_filtrado[df_filtrado["Ano Cancelamento"].isin(anos_selecionados)]

        # Filtrar os registros onde "Status 1" é "ASSINADO" e "Status 2" é "CANCELADO"
        df_distrato = df_filtrado[(df_filtrado["Status 1"] == "ASSINADO") & (df_filtrado["Status 2"] == "CANCELADO")]

        # Somar os valores da coluna "Valor vendido" para esses registros
        distrato_valor = df_distrato["Valor vendido"].sum()

        # Contar a quantidade de distratos
        distrato_quantidade = df_distrato.shape[0]

        # Agrupar distratos por ano e mês
        df_distrato_agrupado = df_distrato.groupby(["Ano Cancelamento", "Mês Cancelamento"]).agg({
            "Valor vendido": "sum",
            "# Clientes": "count"
        }).reset_index()
        df_distrato_agrupado.rename(columns={"Ano Cancelamento": "Ano", "Mês Cancelamento": "Mês"}, inplace=True)

        # Criar gráfico interativo apenas com os valores de distratos
        fig = px.line(
            df_distrato_agrupado,
            x='Mês',
            y='Valor vendido' if mostrar_valor_vendido else '# Clientes',
            color='Ano',
            markers=True,
            title='Evolução dos Distratos por Ano'
        )

        # Ajustar layout para zoom
        fig.update_layout(
            xaxis_title='Mês',
            yaxis_title='Valor Vendido (R$)' if mostrar_valor_vendido else 'Número de Clientes',
            xaxis=dict(
                tickmode='array',
                tickvals=list(range(1, 13)),
                ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
            ),
            yaxis=dict(tickprefix='R$ ' if mostrar_valor_vendido else '', tickformat=',.0f'),
            hovermode='x unified'
        )

        # Exibir gráfico interativo no Streamlit
        st.plotly_chart(fig, use_container_width=True)

        # Exibir valores de distrato
        st.markdown(f"### 🔴 Valor Total de Distratos: R$ {distrato_valor:,.2f}")
        st.markdown(f"### 🔴 Quantidade Total de Distratos: {distrato_quantidade}")









        #########################Distratios UpGrades########################################
       




        # Linha de separação
        st.markdown("---")

        # Título personalizado com HTML e CSS
        st.markdown("""
        <h1 style='color: blue; font-size: 18px;'>DISTRATOS UPGRADES Mês a Mês</h1>
        """, unsafe_allow_html=True)

        # Converter "Data da Venda" para datetime se ainda não estiver
        df_filtrado["Data da Venda"] = pd.to_datetime(df_filtrado["Data da Venda"], errors='coerce')

        # Verificar e converter "Data do cancelamento"
        if "Data do cancelamento" in df_filtrado.columns:
            df_filtrado["Data do cancelamento"] = pd.to_datetime(df_filtrado["Data do cancelamento"], errors='coerce')
        else:
            df_filtrado["Data do cancelamento"] = pd.NaT

        # Criar colunas de Ano e Mês
        df_filtrado["Ano"] = df_filtrado["Data da Venda"].dt.year
        df_filtrado["Mês"] = df_filtrado["Data da Venda"].dt.month

        # Criar colunas de Ano e Mês para cancelamento
        df_filtrado["Ano Cancelamento"] = df_filtrado["Data do cancelamento"].dt.year
        df_filtrado["Mês Cancelamento"] = df_filtrado["Data do cancelamento"].dt.month

        # Criar colunas de Data formatada
        df_filtrado["Data Cancelamento Formatada"] = df_filtrado["Data do cancelamento"].dt.strftime('%Y-%m-%d')

        # Criar lista de anos disponíveis no DataFrame
        anos_disponiveis = sorted(df_filtrado["Ano"].dropna().unique())

        # Criar um seletor no Streamlit para os anos (se aplicável)
        anos_selecionados = st.multiselect(
            "📅 **Selecione os anos para visualizar:**",
            anos_disponiveis,
            default=anos_disponiveis,
            key="anos_selecionados_1"
        )

        # Criar botão para exibir ou ocultar "Valor vendido"
        mostrar_valor_vendido = st.checkbox("Mostrar Valor Vendido", value=True, key="mostrar_valor_vendido_1")

        # Aplicar filtro de anos no DataFrame
        df_filtrado = df_filtrado[df_filtrado["Ano"].isin(anos_selecionados)]

        # Filtrar os registros onde "Status 1" é "ASSINADO" e "Status 2" é "CANCELADO UPGRADE"
        df_distrato = df_filtrado[(df_filtrado["Status 1"] == "ASSINADO") & (df_filtrado["Status 2"] == "CANCELADO UPGRADE")]

        # Somar os valores da coluna "Valor vendido" para esses registros
        distrato_valor = df_distrato["Valor vendido"].sum()

        # Contar a quantidade de distratos
        distrato_quantidade = df_distrato.shape[0]

        # Agrupar vendas "À Vista"
        df_vendas_agrupadas = df_filtrado.groupby(["Ano", "Mês"]).agg({
            "Valor vendido": "sum",
            "# Clientes": "sum"
        }).reset_index()

        # Agrupar distratos
        df_distrato_agrupado = df_distrato.groupby(["Ano Cancelamento", "Mês Cancelamento"]).agg({
            "Valor vendido": "sum",
            "# Clientes": "count"
        }).reset_index()
        df_distrato_agrupado.rename(columns={"Ano Cancelamento": "Ano", "Mês Cancelamento": "Mês"}, inplace=True)

        # Criar gráfico interativo com Plotly
        fig = px.line(
            df_vendas_agrupadas,
            x='Mês',
            y='Valor vendido',
            color='Ano',
            markers=True,
            title='Evolução das Vendas e Distratos Upgrades por Ano'
        )

        # Adicionar linha de distratos
        if not df_distrato_agrupado.empty:
            fig.add_scatter(
                x=df_distrato_agrupado['Mês'],
                y=df_distrato_agrupado['Valor vendido'],
                mode='lines+markers',
                name='Distratos Upgrades',
                text=df_distrato_agrupado['Mês'].astype(str) + '/' + df_distrato_agrupado['Ano'].astype(str),
                hoverinfo='text+y',
                line=dict(dash='dash', color='red')
            )

        # Ajustar layout para zoom
        fig.update_layout(
            xaxis_title='Mês',
            yaxis_title='Valor Vendido (R$)',
            xaxis=dict(tickmode='array', tickvals=list(range(1, 13)), ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']),
            yaxis=dict(tickprefix='R$ ', tickformat=',.0f'),
            hovermode='x unified'
        )

        # Exibir gráfico interativo no Streamlit
        st.plotly_chart(fig, use_container_width=True)

        # Exibir valores de distrato
        st.markdown(f"### 🔴 Valor Total de Distratos Upgrades: R$ {distrato_valor:,.2f}")
        st.markdown(f"### 🔴 Quantidade Total de Distratos Upgrades: {distrato_quantidade}")



########################################GRafico animado#######################

 # PÁGINA GRÁFICOS DISTRATOS
if pagina == 'Previsão de Vendas':
    st.title('📈 Ranking Corretores')
    if not df_filtrado.empty:















        # Lendo o arquivo XLSX
        #df = pd.read_excel('claro_HG_VENDAS_PY.xlsx')

        # Título do Dashboard
        st.title("Previsão de Vendas por GERENTE - 2025")

        # Verificar valores nulos
        nulos_data = df['Data da Venda'].isnull().sum()
        nulos_gerente = df['GERENTE'].isnull().sum()

        # Exibir contagem de valores nulos
        st.write(f"**Valores Nulos em 'Data da Venda':** {nulos_data}")
        st.write(f"**Valores Nulos em 'GERENTE':** {nulos_gerente}")

        # Converter datas e extrair ano/mês
        df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])
        df['Ano'] = df['Data da Venda'].dt.year
        df['Mês'] = df['Data da Venda'].dt.month

        # Filtrar apenas os anos de 2022, 2023 e 2024
        df = df[df['Ano'].isin([2022, 2023, 2024])]

        # Remover registros com dados nulos em colunas essenciais
        df = df.dropna(subset=['Data da Venda', 'GERENTE'])

        # Agrupar vendas por Ano, Mês e GERENTE
        df_grouped = df.groupby(['Ano', 'Mês', 'GERENTE']).size().reset_index(name='Vendas')

        # Exibir estatísticas básicas
        estatisticas_vendas = df_grouped.groupby(['Ano', 'GERENTE'])['Vendas'].sum().reset_index()
        st.write("**Total de Vendas por Ano e GERENTE:**")
        st.write(estatisticas_vendas)

        # Codificar 'GERENTE' para o modelo
        df_grouped['GERENTE_Cod'] = pd.factorize(df_grouped['GERENTE'])[0]

        # Features e target
        X = df_grouped[['Ano', 'Mês', 'GERENTE_Cod']]
        y = df_grouped['Vendas']

        # Treinar modelo de Regressão Linear
        model = LinearRegression()
        model.fit(X, y)

        # Criar dados para 2025 para cada GERENTE
        gerentes = df_grouped['GERENTE'].unique()
        meses = np.arange(1, 13)

        # DataFrame para armazenar previsões de 2025
        previsoes_2025 = pd.DataFrame()

        for gerente in gerentes:
            gerente_cod = pd.factorize(df_grouped['GERENTE'])[0][df_grouped['GERENTE'] == gerente][0]
            ano_2025 = np.full(12, 2025)
            gerente_array = np.full(12, gerente_cod)

            X_2025 = pd.DataFrame({
                'Ano': ano_2025,
                'Mês': meses,
                'GERENTE_Cod': gerente_array
            })

            pred_2025 = model.predict(X_2025)

            df_temp = pd.DataFrame({
                'Ano': 2025,
                'Mês': meses,
                'GERENTE': gerente,
                'Previsão de Vendas': pred_2025.astype(int)
            })

            previsoes_2025 = pd.concat([previsoes_2025, df_temp])

        # Criar o gráfico interativo com Plotly
        fig = px.line(previsoes_2025, 
                    x='Mês', 
                    y='Previsão de Vendas', 
                    color='GERENTE', 
                    markers=True,
                    title='Previsão de Vendas por GERENTE - 2025',
                    labels={'Mês': 'Mês', 'Previsão de Vendas': 'Número de Vendas'})

        # Adicionar hover e rótulos de valores
        fig.update_traces(mode='lines+markers+text', 
                        text=previsoes_2025['Previsão de Vendas'],
                        textposition='top center',
                        hovertemplate='Mês: %{x}<br>Vendas: %{y}<br>GERENTE: %{legendgroup}')

        # Configurações adicionais do gráfico
        fig.update_layout(legend_title_text='GERENTE', 
                        hovermode='x unified',
                        xaxis_title='Mês',
                        yaxis_title='Número de Vendas')

        # Exibir gráfico interativo
        st.plotly_chart(fig)

        # Exibir a tabela de previsões
        st.write("Previsão de Vendas para 2025 por GERENTE:")
        st.dataframe(previsoes_2025)









        # Análise inicial dos dados de vendas com Campanha
        st.title("Previsão de Vendas por Campanha - 2025")

        # Verificar valores nulos
        nulos_data = df['Data da Venda'].isnull().sum()
        nulos_campanha = df['Campanha'].isnull().sum()

        # Exibir contagem de valores nulos
        st.write(f"**Valores Nulos em 'Data da Venda':** {nulos_data}")
        st.write(f"**Valores Nulos em 'Campanha':** {nulos_campanha}")

        # Converter 'Data da Venda' para datetime e extrair ano e mês
        df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])
        df['Ano'] = df['Data da Venda'].dt.year
        df['Mês'] = df['Data da Venda'].dt.month

        # Filtrar apenas os anos de 2022, 2023 e 2024
        df = df[df['Ano'].isin([2022, 2023, 2024])]

        # Remover registros com dados nulos em colunas essenciais
        df = df.dropna(subset=['Data da Venda', 'Campanha'])

        # Agrupar vendas por Ano, Mês e Campanha
        df_grouped = df.groupby(['Ano', 'Mês', 'Campanha']).size().reset_index(name='Vendas')

        # Codificar 'Campanha' para o modelo
        df_grouped['Campanha Cod'] = pd.factorize(df_grouped['Campanha'])[0]

        # Features e target
        X = df_grouped[['Ano', 'Mês', 'Campanha Cod']]
        y = df_grouped['Vendas']

        # Treinar modelo de Regressão Linear
        model = LinearRegression()
        model.fit(X, y)

        # Criar dados para 2025 para cada Campanha
        campanhas = df_grouped['Campanha'].unique()
        meses = np.arange(1, 13)

        # DataFrame para armazenar previsões de 2025
        previsoes_2025 = pd.DataFrame()

        for campanha in campanhas:
            campanha_cod = pd.factorize(df_grouped['Campanha'])[0][df_grouped['Campanha'] == campanha][0]
            ano_2025 = np.full(12, 2025)
            campanha_array = np.full(12, campanha_cod)

            X_2025 = pd.DataFrame({
                'Ano': ano_2025,
                'Mês': meses,
                'Campanha Cod': campanha_array
            })

            pred_2025 = model.predict(X_2025)
            
            df_temp = pd.DataFrame({
                'Ano': 2025,
                'Mês': meses,
                'Campanha': campanha,
                'Previsão de Vendas': pred_2025.astype(int)
            })

            previsoes_2025 = pd.concat([previsoes_2025, df_temp])

        # Criar o gráfico apenas com previsões de 2025
        st.title("Previsão de Vendas para 2025 por Campanha")
        fig, ax = plt.subplots(figsize=(14, 7))

        # Plotar apenas as previsões para 2025 por Campanha
        for campanha in campanhas:
            df_pred = previsoes_2025[previsoes_2025['Campanha'] == campanha]
            ax.plot(df_pred['Mês'], df_pred['Previsão de Vendas'], marker='*', linestyle='--', label=f'2025 - {campanha}')
            for i, value in enumerate(df_pred['Previsão de Vendas']):
                ax.annotate(f'{value}', (df_pred['Mês'].values[i], value), textcoords="offset points", xytext=(0,10), ha='center')

        # Configurar o gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Número de Vendas')
        ax.set_title('Previsão de Vendas por Campanha - 2025')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

        # Posicionar legenda em duas linhas na parte superior interna do gráfico
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=4, fontsize='small', frameon=False)

        # Exibir o gráfico
        st.pyplot(fig)

        # Exibir tabela com previsões para 2025
        st.write("Previsão de Vendas para 2025 por Campanha:")
        st.dataframe(previsoes_2025)















        # Remover espaços nos nomes das colunas
        df.columns = df.columns.str.replace(' ', '')

        # Análise inicial dos dados de vendas por Corretor 1
        st.title("Previsão de Vendas por Corretor 1 - 2025")

        # Verificar valores nulos
        nulos_data = df['DatadaVenda'].isnull().sum()

        # Exibir contagem de valores nulos
        st.write(f"**Valores Nulos em 'Data da Venda':** {nulos_data}")

        # Converter 'Data da Venda' para datetime e extrair ano e mês
        df['DatadaVenda'] = pd.to_datetime(df['DatadaVenda'])
        df['Ano'] = df['DatadaVenda'].dt.year
        df['Mês'] = df['DatadaVenda'].dt.month

        # Filtrar apenas os anos de 2022, 2023 e 2024
        df_filtrado = df[df['Ano'].isin([2022, 2023, 2024])]

        # Agrupar vendas por Ano, Mês e Corretor 1
        df_grouped = df_filtrado.groupby(['Ano', 'Mês', 'Corretor1']).size().reset_index(name='Vendas')

        # Codificar 'Corretor 1' para o modelo
        df_grouped['Corretor_Cod'] = pd.factorize(df_grouped['Corretor1'])[0]

        # Features e target
        X = df_grouped[['Ano', 'Mês', 'Corretor_Cod']]
        y = df_grouped['Vendas']

        # Treinar modelo de Regressão Linear
        model = LinearRegression()
        model.fit(X, y)

        # Criar dados para 2025 para cada Corretor
        corretores = df_grouped['Corretor1'].unique()
        meses = np.arange(1, 13)

        # DataFrame para armazenar previsões de 2025
        previsoes_2025 = pd.DataFrame()

        for corretor in corretores:
            corretor_cod = pd.factorize(df_grouped['Corretor1'])[0][df_grouped['Corretor1'] == corretor][0]
            ano_2025 = np.full(12, 2025)
            corretor_array = np.full(12, corretor_cod)

            X_2025 = pd.DataFrame({
                'Ano': ano_2025,
                'Mês': meses,
                'Corretor_Cod': corretor_array
            })

            pred_2025 = model.predict(X_2025)
            
            df_temp = pd.DataFrame({
                'Ano': 2025,
                'Mês': meses,
                'Corretor1': corretor,
                'Previsão_de_Vendas': pred_2025.astype(int)
            })

            previsoes_2025 = pd.concat([previsoes_2025, df_temp])

        # Criar o gráfico apenas com previsões de 2025
        st.title("Previsão de Vendas para 2025 por Corretor")
        fig, ax = plt.subplots(figsize=(14, 7))

        # Plotar apenas as previsões para 2025 por Corretor 1
        for corretor in corretores:
            df_pred = previsoes_2025[previsoes_2025['Corretor1'] == corretor]
            ax.plot(df_pred['Mês'], df_pred['Previsão_de_Vendas'], marker='*', linestyle='--', label=f'2025 - {corretor}')
            for i, value in enumerate(df_pred['Previsão_de_Vendas']):
                ax.annotate(f'{value}', (df_pred['Mês'].values[i], value), textcoords="offset points", xytext=(0,10), ha='center')

        # Configurar o gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Número de Vendas')
        ax.set_title('Previsão de Vendas por Corretor - 2025')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

        # Posicionar legenda em duas linhas na parte superior interna do gráfico
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=4, fontsize='small', frameon=False)

        # Exibir o gráfico
        st.pyplot(fig)

        # Exibir tabela com previsões para 2025
        st.write("Previsão de Vendas para 2025 por Corretor:")
        st.dataframe(previsoes_2025)









        # Remover espaços nos nomes das colunas
        df.columns = df.columns.str.replace(' ', '')

        # Análise inicial dos dados de vendas com GERENTE
        st.title("Previsão de Vendas por GERENTE - 2026")

        # Verificar valores nulos
        nulos_data = df['DatadaVenda'].isnull().sum()
        nulos_gerente = df['GERENTE'].isnull().sum()

        # Verificar estatísticas básicas
        df['Ano'] = df['DatadaVenda'].dt.year

        # Remover registros com dados nulos em colunas essenciais
        df = df.dropna(subset=['DatadaVenda', 'GERENTE'])

        # Criar coluna para o mês
        df['Mês'] = df['DatadaVenda'].dt.month

        # Agrupar vendas por Ano, Mês e GERENTE
        df_grouped = df.groupby(['Ano', 'Mês', 'GERENTE']).size().reset_index(name='Vendas')

        # Codificar 'GERENTE' para o modelo
        df_grouped['GERENTE_Cod'] = pd.factorize(df_grouped['GERENTE'])[0]

        # Features e target
        X = df_grouped[['Ano', 'Mês', 'GERENTE_Cod']]
        y = df_grouped['Vendas']

        # Treinar modelo de Regressão Linear
        model = LinearRegression()
        model.fit(X, y)

        # Criar dados para 2026 para cada GERENTE
        gerentes = df_grouped['GERENTE'].unique()
        meses = np.arange(1, 13)

        # DataFrame para armazenar previsões de 2026
        previsoes_2026 = pd.DataFrame()

        for gerente in gerentes:
            gerente_cod = pd.factorize(df_grouped['GERENTE'])[0][df_grouped['GERENTE'] == gerente][0]
            ano_2026 = np.full(12, 2026)
            gerente_array = np.full(12, gerente_cod)

            X_2026 = pd.DataFrame({
                'Ano': ano_2026,
                'Mês': meses,
                'GERENTE_Cod': gerente_array
            })

            pred_2026 = model.predict(X_2026)
            
            df_temp = pd.DataFrame({
                'Ano': 2026,
                'Mês': meses,
                'GERENTE': gerente,
                'Previsão de Vendas': pred_2026.astype(int)
            })

            previsoes_2026 = pd.concat([previsoes_2026, df_temp])

        # Criar o gráfico apenas com previsões de 2026
        st.title("Previsão de Vendas para 2026 por GERENTE")
        fig, ax = plt.subplots(figsize=(14, 7))

        # Plotar apenas as previsões para 2026 por GERENTE
        for gerente in gerentes:
            df_pred = previsoes_2026[previsoes_2026['GERENTE'] == gerente]
            ax.plot(df_pred['Mês'], df_pred['Previsão de Vendas'], marker='*', linestyle='--', label=f'2026 - {gerente}')
            for i, value in enumerate(df_pred['Previsão de Vendas']):
                ax.annotate(f'{value}', (df_pred['Mês'].values[i], value), textcoords="offset points", xytext=(0,10), ha='center')

        # Configurar o gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Número de Vendas')
        ax.set_title('Previsão de Vendas por GERENTE - 2026')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

        # Posicionar legenda em duas linhas na parte superior interna do gráfico
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=4, fontsize='small', frameon=False)

        # Exibir o gráfico
        st.pyplot(fig)

        # Exibir tabela com previsões para 2026
        st.write("Previsão de Vendas para 2026 por GERENTE:")
        st.dataframe(previsoes_2026)


            




        # Análise inicial dos dados de vendas com Campanha
        st.title("Previsão de Vendas por Campanha - 2026 HG")

        # Verificar valores nulos
        nulos_data = df['DatadaVenda'].isnull().sum()
        nulos_campanha = df['Campanha'].isnull().sum()

        # Verificar estatísticas básicas
        df['Ano'] = pd.to_datetime(df['DatadaVenda']).dt.year

        # Remover registros com dados nulos em colunas essenciais
        df = df.dropna(subset=['DatadaVenda', 'Campanha'])

        # Criar coluna para o mês
        df['Mês'] = pd.to_datetime(df['DatadaVenda']).dt.month

        # Agrupar vendas por Ano, Mês e Campanha
        df_grouped = df.groupby(['Ano', 'Mês', 'Campanha']).size().reset_index(name='Vendas')

        # Codificar 'Campanha' para o modelo
        df_grouped['Campanha Cod'], _ = pd.factorize(df_grouped['Campanha'])

        # Features e target
        X = df_grouped[['Ano', 'Mês', 'Campanha Cod']]
        y = df_grouped['Vendas']

        # Treinar modelo de Regressão Linear
        model = LinearRegression()
        model.fit(X, y)

        # Criar dados para 2026 para cada Campanha
        campanhas = df_grouped['Campanha'].unique()
        meses = np.arange(1, 13)

        # DataFrame para armazenar previsões de 2026
        previsoes_2026 = pd.DataFrame()

        for campanha in campanhas:
            campanha_cod = df_grouped.loc[df_grouped['Campanha'] == campanha, 'Campanha Cod'].values[0]
            ano_2026 = np.full(12, 2026)
            campanha_array = np.full(12, campanha_cod)

            X_2026 = pd.DataFrame({
                'Ano': ano_2026,
                'Mês': meses,
                'Campanha Cod': campanha_array
            })

            pred_2026 = model.predict(X_2026)
            
            df_temp = pd.DataFrame({
                'Ano': 2026,
                'Mês': meses,
                'Campanha': campanha,
                'Previsão de Vendas': pred_2026.astype(int)
            })

            previsoes_2026 = pd.concat([previsoes_2026, df_temp], ignore_index=True)

        # Criar o gráfico apenas com previsões de 2026
        st.title("Previsão de Vendas para 2026 por Campanha")
        fig, ax = plt.subplots(figsize=(14, 7))

        # Plotar apenas as previsões para 2026 por Campanha
        for campanha in campanhas:
            df_pred = previsoes_2026[previsoes_2026['Campanha'] == campanha]
            ax.plot(df_pred['Mês'], df_pred['Previsão de Vendas'], marker='*', linestyle='--', label=f'2026 - {campanha}')
            for i, value in enumerate(df_pred['Previsão de Vendas']):
                ax.annotate(f'{value}', (df_pred['Mês'].values[i], value), textcoords="offset points", xytext=(0,10), ha='center')

        # Configurar o gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Número de Vendas')
        ax.set_title('Previsão de Vendas por Campanha - 2026')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

        # Posicionar legenda em duas linhas na parte superior interna do gráfico
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=4, fontsize='small', frameon=False)

        # Exibir o gráfico
        st.pyplot(fig)

        # Exibir tabela com previsões para 2026
        st.write("Previsão de Vendas para 2026 por Campanha:")
        st.dataframe(previsoes_2026)







###############################Previsão de vendas#############################





        # Verificar valores nulos
        nulos_data = df['DatadaVenda'].isnull().sum()
        nulos_campanha = df['Campanha'].isnull().sum()
        nulos_origem = df['Origemdavenda'].isnull().sum()

        # Verificar estatísticas básicas
        df['Ano'] = pd.to_datetime(df['DatadaVenda']).dt.year
        df['Mês'] = pd.to_datetime(df['DatadaVenda']).dt.month
        estatisticas_vendas = df.groupby(['Ano', 'Mês', 'Campanha', 'Origemdavenda']).size().reset_index(name='Total de Vendas')

        # Exibir análise inicial
        st.write(f"**Valores Nulos em 'DatadaVenda':** {nulos_data}")
        st.write(f"**Valores Nulos em 'Campanha':** {nulos_campanha}")
        st.write(f"**Valores Nulos em 'Origem da Venda':** {nulos_origem}")
        st.write("**Total de Vendas por Ano, Mês, Campanha e Origem da Venda:**")
        st.write(estatisticas_vendas)

        # Remover registros com dados nulos em colunas essenciais
        df = df.dropna(subset=['DatadaVenda', 'Campanha', 'Origemdavenda'])

        # Agrupar vendas por Ano, Mês, Campanha e Origem da Venda
        df_grouped = df.groupby(['Ano', 'Mês', 'Campanha', 'Origemdavenda']).size().reset_index(name='Vendas')

        # Adicionar seletores
        anos_disponiveis = ["Todos"] + sorted(df_grouped['Ano'].unique())
        campanhas_disponiveis = ["Todas"] + sorted(df_grouped['Campanha'].unique())
        origens_disponiveis = ["Todas"] + sorted(df_grouped['Origemdavenda'].unique())

        ano_selecionado = st.selectbox("Selecione o Ano:", anos_disponiveis)
        campanha_selecionada = st.selectbox("Selecione a Campanha:", campanhas_disponiveis)
        origem_selecionada = st.selectbox("Selecione a Origem da Venda:", origens_disponiveis)

        # Filtrar dados conforme seleções
        df_filtrado = df_grouped.copy()
        if ano_selecionado != "Todos":
            df_filtrado = df_filtrado[df_filtrado['Ano'] == ano_selecionado]

        if campanha_selecionada != "Todas":
            df_filtrado = df_filtrado[df_filtrado['Campanha'] == campanha_selecionada]

        if origem_selecionada != "Todas":
            df_filtrado = df_filtrado[df_filtrado['Origemdavenda'] == origem_selecionada]

        # Criar modelo de regressão baseado nos dados filtrados
        if not df_filtrado.empty:
            X_treino = df_filtrado[['Ano', 'Mês']]
            y_treino = df_filtrado['Vendas']

            model = LinearRegression()
            model.fit(X_treino, y_treino)

            # Criar previsões para 2025
            meses = np.arange(1, 13)
            ano_2025 = np.full(12, 2025)
            X_2025 = pd.DataFrame({'Ano': ano_2025, 'Mês': meses})
            previsoes_2025 = model.predict(X_2025)

            # Criar DataFrame das previsões
            df_previsoes_2025 = pd.DataFrame({'Ano': 2025, 'Mês': meses, 'Vendas Previstas': previsoes_2025.astype(int)})

            # Criar gráfico atualizado conforme os filtros
            st.title("Evolução Mensal das Vendas e Previsão para 2025")
            fig, ax = plt.subplots(figsize=(14, 7))

            for ano in df_filtrado['Ano'].unique():
                df_ano = df_filtrado[df_filtrado['Ano'] == ano]
                ax.plot(df_ano['Mês'], df_ano['Vendas'], marker='o', linestyle='-', label=f'Vendas {ano}')
                for i, value in enumerate(df_ano['Vendas']):
                    ax.annotate(f'{value}', (df_ano['Mês'].values[i], value), textcoords="offset points", xytext=(0,10), ha='center')

            # Adicionar previsão de 2025
            ax.plot(df_previsoes_2025['Mês'], df_previsoes_2025['Vendas Previstas'], marker='*', linestyle='--', color='red', label='Previsão 2025')
            for i, value in enumerate(df_previsoes_2025['Vendas Previstas']):
                ax.annotate(f'{value}', (df_previsoes_2025['Mês'].values[i], value), textcoords="offset points", xytext=(0,10), ha='center')

            # Criar linha de tendência global
            df_tendencia = df_filtrado.groupby('Mês')['Vendas'].mean().reset_index()
            ax.plot(df_tendencia['Mês'], df_tendencia['Vendas'], linestyle='--', color='gray', label='Tendência Global')

            # Configurar o gráfico
            ax.set_xlabel('Mês')
            ax.set_ylabel('Número de Vendas')
            ax.set_title('Evolução das Vendas e Previsão para 2025')
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.set_xticks(range(1, 13))
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
            ax.legend()

            # Exibir gráfico
            st.pyplot(fig)

            # Exibir tabela com previsões para 2025
            st.write("Previsão de Vendas para 2025:")
            st.dataframe(df_previsoes_2025)






###############################Fim Previsão de vendas##########################
            
       


    

        # Carregando o DataFrame
        df_data = pd.read_excel('BASERESGATE.xlsx')

        # Título da página
        st.title("Filtro de Dados com Selectbox")

        # Verificando se a coluna "Origem da venda" existe no DataFrame
        if "Origem da venda" in df_data.columns:
            # Removendo valores nulos da coluna "Origem da venda"
            origens_venda = df_data["Origem da venda"].dropna().unique()

            # Adicionando um selectbox para filtrar por origem da venda
            origem_selecionada = st.selectbox("Selecione Origem da venda:", origens_venda)

            # Filtrando o DataFrame com base na origem selecionada
            df_filtrado = df_data[df_data["Origem da venda"] == origem_selecionada].copy()

            # Removendo nomes repetidos na coluna "Corretor 1"
            df_filtrado_sem_repetidos = df_filtrado.drop_duplicates(subset=["Corretor 1"])

            # Exibindo o DataFrame filtrado sem nomes repetidos
            st.write("Dados filtrados (sem nomes repetidos):")
            st.dataframe(df_filtrado_sem_repetidos[["Corretor 1", "Valor vendido"]])

            # Calculando e exibindo os totais
            st.write("Totais:")
            total_vendido = df_filtrado["Valor vendido"].sum()
            st.write(f"Total Vendido: **R$ {total_vendido:,.2f}**")  # Formatação para moeda

            # Criando o gráfico de barras para a coluna "Valor vendido" usando Plotly ou Matplotlib
            import plotly.express as px
            fig = px.bar(df_filtrado, x="Corretor 1", y="Valor vendido", title="Valor Vendido por Corretor")
            st.plotly_chart(fig)

        else:
            st.error("A coluna 'Origem da venda' não foi encontrada no DataFrame.")


            

        #df_data
      
        
 # PÁGINA GRÁFICOS DISTRATOS
if pagina == 'Simulador':
    st.title('📈 Testes')
    if not df_filtrado.empty:

        import pandas as pd
        import streamlit as st

        # Garantir que "Data da Venda" está no formato datetime
        df_filtrado["Data da Venda"] = pd.to_datetime(df_filtrado["Data da Venda"], errors="coerce")

        # Selecionar as colunas desejadas
        columns_selected = [
            "Data da Venda", "Status 2", "# Clientes", "Valor vendido",
            "Desconto Financeiro", "Desconto Real Viabilidade", "Ganho Viabilidade", "De Entrada"
        ]

        # Garantir que as colunas selecionadas existem no DataFrame
        columns_selected = [col for col in columns_selected if col in df_filtrado.columns]

        # Filtrar apenas registros com "ATIVO" na coluna "Status 2"
        df_selected = df_filtrado[df_filtrado["Status 2"] == "ATIVO"][columns_selected].copy()

        # Criar colunas para Ano e Mês
        df_selected["Ano"] = df_selected["Data da Venda"].dt.year
        df_selected["Mês"] = df_selected["Data da Venda"].dt.month.fillna(0).astype(int)

        # Definir colunas de quantidades e valores monetários
        quantidade_columns = ["# Clientes"]
        valor_columns = ["Valor vendido", "Desconto Financeiro", "Desconto Real Viabilidade", "Ganho Viabilidade", "De Entrada"]

        # Converter colunas corretamente
        for col in quantidade_columns:
            if col in df_selected.columns:
                df_selected[col] = pd.to_numeric(df_selected[col], errors="coerce").fillna(0).astype(int)

        for col in valor_columns:
            if col in df_selected.columns:
                df_selected[col] = pd.to_numeric(df_selected[col], errors="coerce").fillna(0)

        # Criar tabelas separadas por mês e ano, com totais fixos
        tables_by_month = {}
        for year in sorted(df_selected["Ano"].dropna().unique()):
            for month in sorted(df_selected[df_selected["Ano"] == year]["Mês"].dropna().unique()):
                table_name = f"Tabela - {year}/{int(month):02d}"

                # Filtrar dados do mês específico
                df_month = df_selected[(df_selected["Ano"] == year) & (df_selected["Mês"] == month)]

                # Calcular totais para o mês
                totals = df_month[quantidade_columns + valor_columns].sum().to_frame().T
                totals["Data da Venda"] = "TOTAL"
                totals["Status 2"] = "TOTAL"

                # Fixar a linha de totais na última linha da tabela
                df_month = pd.concat([df_month, totals], ignore_index=True)
                tables_by_month[table_name] = df_month

        # Calcular totais gerais
        totals_overall = df_selected[quantidade_columns + valor_columns].sum().to_frame().T

        totals_overall["Data da Venda"] = "TOTAL GERAL"
        totals_overall["Status 2"] = "TOTAL GERAL"

        # 🔹 Função para destacar a linha de totais com fundo verde
        def highlight_totals(s):
            return ["background-color: lightgreen" if s["Data da Venda"] in ["TOTAL", "TOTAL GERAL"] else "" for _ in s]

        # Exibir tabelas no Streamlit
        st.title("📊 Relatório Mensal com Totais Fixos e Destaque")

        for name, table in tables_by_month.items():
            st.subheader(name)
            st.dataframe(
                table.style.apply(highlight_totals, axis=1).format({
                    col: "{:,}".replace(",", ".") for col in quantidade_columns  # Sem casas decimais, formato correto
                }).format({
                    col: "R$ {:,.2f}" for col in valor_columns  # Com casas decimais
                })
            )

        # Exibir totais gerais
        st.subheader("📊 Totais Gerais")
        st.dataframe(
            totals_overall.style.apply(highlight_totals, axis=1).format({
                col: "{:,}".replace(",", ".") for col in quantidade_columns  # Sem casas decimais, formato correto
            }).format({
                col: "R$ {:,.2f}" for col in valor_columns  # Com casas decimais
            })
        )
        # Definindo os valores fornecidos
        valor_vendido = 62106932  # Valor total vendido
        desconto_financeiro = 2364155  # Desconto financeiro aplicado

        # Calculando o percentual de desconto em relação ao valor vendido
        percentual_desconto = (desconto_financeiro / valor_vendido) * 100
                    
        # Exibindo o resultado
        percentual_desconto
      


      ######################################CORREÇÂO TABELA############################



        # Função para formatação monetária segura
        def format_currency(value):
            try:
                return f'R$ {float(value):,.2f}'
            except (ValueError, TypeError):
                return 'R$ 0,00'

        # Função aprimorada para carregar dados
        def load_data():
            required_columns = [
                'Data da Venda', 'Status 2', '# Clientes', 'Valor vendido',
                'Desconto Financeiro', 'Desconto Real Viabilidade',
                'Ganho Viabilidade', 'De Entrada'
            ]
            
            try:
                df = pd.read_excel(
                    'BASEOFICIAL.xlsx',
                    sheet_name='Consulta Contratos',
                    parse_dates=['Data da Venda'],
                    usecols=required_columns
                )
                
                if df.empty:
                    st.error("Planilha 'Consulta Contratos' está vazia")
                    return None
                    
                numeric_cols = ['Valor vendido', 'Desconto Financeiro', 
                            'Desconto Real Viabilidade', 'Ganho Viabilidade', 
                            '# Clientes', 'De Entrada']
                
                df[numeric_cols] = df[numeric_cols].apply(
                    pd.to_numeric, errors='coerce'
                ).fillna(0)
                
                return df

            except FileNotFoundError:
                st.error("Arquivo BASEOFICIAL.xlsx não encontrado")
                return None
            except Exception as e:
                st.error(f"Erro crítico ao carregar dados: {str(e)}")
                return None

        # Função otimizada para cálculo de métricas
        def calculate_metrics(df):
            df = df[df['Status 2'] == 'ATIVO'].copy()
            df['Data da Venda'] = pd.to_datetime(
                df['Data da Venda'], errors='coerce'
            ).dropna()
            df['Ano'] = df['Data da Venda'].dt.year
            df['Mês'] = df['Data da Venda'].dt.month
            
            date_grid = pd.MultiIndex.from_product(
                [df['Ano'].unique(), range(1,13)],
                names=['Ano', 'Mês']
            ).to_frame(index=False)
            
            agg_params = {
                '# Clientes': 'sum',
                'Valor vendido': 'sum',
                'Desconto Financeiro': 'sum',
                'Desconto Real Viabilidade': 'sum',
                'Ganho Viabilidade': 'sum',
                'De Entrada': 'mean'
            }
            
            grouped = df.groupby(['Ano', 'Mês']).agg(agg_params).reset_index()
            
            merged = date_grid.merge(
                grouped,
                on=['Ano', 'Mês'],
                how='left'
            ).fillna(0)
            
            merged['DESCONTO TOTAL'] = merged['Desconto Financeiro'] + merged['Desconto Real Viabilidade']
            merged['Ganho/Perda'] = merged['Ganho Viabilidade'] - merged['Desconto Real Viabilidade']
            
            merged['Desconto Médio Financeiro (%)'] = (merged['Desconto Financeiro'] / merged['Valor vendido'].replace(0, 1)) * 100
            
            merged['Ticket Médio'] = merged['Valor vendido'].div(
                merged['# Clientes'].replace(0, 1)
            )
            
            return merged

        # Função para exibição otimizada
        def display_tables(data):
            st.title('📈 Análise Comercial Detalhada')
            
            for year in sorted(data['Ano'].unique(), reverse=True):
                st.subheader(f"Ano {int(year)}")
                year_data = data[data['Ano'] == year].copy()
                
                meses = [
                    'Janeiro', 'Fevereiro', 'Março', 'Abril',
                    'Maio', 'Junho', 'Julho', 'Agosto',
                    'Setembro', 'Outubro', 'Novembro', 'Dezembro'
                ]
                year_data['Mês'] = year_data['Mês'].map(
                    lambda x: meses[int(x)-1] if 1 <= x <=12 else 'Inválido'
                )
                
                totals = year_data.sum(numeric_only=True)
                totals['Mês'] = 'TOTAL ANUAL'
                totals['De Entrada'] = year_data['De Entrada'].mean()
                
                format_cols = [
                    'Valor vendido', 'Desconto Financeiro',
                    'Desconto Real Viabilidade', 'Ganho Viabilidade',
                    'DESCONTO TOTAL', 'Ganho/Perda', 'Desconto Médio Financeiro (%)', 'Ticket Médio'
                ]
                
                for col in format_cols:
                    if "Desconto Médio Financeiro" in col:
                        year_data[col] = year_data[col].apply(lambda x: f"{x:.2f}%")
                        totals[col] = f"{totals[col]:.2f}%"
                    else:
                        year_data[col] = year_data[col].apply(format_currency)
                        totals[col] = format_currency(totals[col])
                
                totals['De Entrada'] = f"{totals['De Entrada']:.2f}%"
                
                styled_df = pd.concat([year_data, totals.to_frame().T], ignore_index=True)
                
                def highlight_totals(row):
                    if row['Mês'] == 'TOTAL ANUAL':
                        return ['background-color: lightgreen'] * len(row)
                    return [''] * len(row)
                
                styled_df = styled_df.style.apply(highlight_totals, axis=1)
                
                st.dataframe(styled_df, use_container_width=True)

        if __name__ == '__main__':
            raw_data = load_data()
            
            if raw_data is not None:
                processed_data = calculate_metrics(raw_data)
                
                if not processed_data.empty:
                    display_tables(processed_data)
                else:
                    st.warning("Nenhum dado válido para análise")
