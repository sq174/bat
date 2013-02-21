@echo off

for %%A in (\D:temp/*.LOG) do (

	for /f "delims=# skip=1" %%L in (%%A) do (
		set FILENAME = %%L

		goto EXIT_FOR
	)
:EXIT_FOR
copy %%A %FILENAME:/=-%.LOG

)
pause