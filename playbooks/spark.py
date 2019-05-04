
SPARK_ACCESS_TOKEN = "ZDM5N2VjYjItMTQzOC00ODllLWI5N2YtMzMyN2M4NzMzOTg4MzUzOGEzZWQtMDRi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
SPARK_ROOM_ID="Y2lzY29zcGFyazovL3VzL1JPT00vZDZmMTIzODQtYjA2Yy0zNzkzLWFhN2MtMjI1YWQyYjZlNTA0"

spark = ciscosparkapi.CiscoSparkAPI(SPARK_ACCESS_TOKEN)

message = spark.messages.create(SPARK_ROOM_ID,
  text='MISSION: 0day Umbrella-Investigate - I have completed the Umbrella Investigate mission!')
  print(message)
