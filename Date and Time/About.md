1. The time module
   * Begins recording time from the epoch that begins at 00:00:00, 1st Jan 1970
   
   | Function | Description |
   | -------- | ----------- |
   | time()   | Returns the number of seconds |
   | ctime()  | Returns the current date and time |
   | sleep()  | Stops execution of a thread for the given duration |
   | localtime() | Returns the date and time in time.struct_time format |
   | gmtime() | Returns time.struct_time in UTC format |
   | mktime() | Returns the seconds passed since epoch pas output |
   | asctime()| Returns a string representing the same |

   * Attributes of struct_time class
   
   | Attribute | Value |
   | --------- | ----- |
   | tm_year   | 0000, ...,2019, ...,9999 |
   | tm_mon    | 1-12  |
   | tm_mday   | 1-31  |
   | tm_hour   | 0-23  |
   | tm_min    | 0-59  |
   | tm_sec    | 0-61  |
   | tm_wday   | 0-6, Monday as 0 |
   | tm_yday   | 1-366 |
   | tm_isdst  | 0, 1, -1 |

2. The datetime module
   | Function | Description |
   | -------- | ----------- |
   | datetime() | Datetime constructor |
   | datetime.today() | Returns the current date and time |
   | datetime.now() | Returns the current date and time |
   | date() | Takes year, month and day as parameter and creates the corresponding date |
   | time() | Takes hour, min, sec, microseconds and tzinfo as parameter and creates the corresponding date |
   | datetime.fromstamp() | Converts seconds to return the corresponding date and time |
   | timedelta() | It is the difference between different dates or times(Duration) |
