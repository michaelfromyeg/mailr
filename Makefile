# run as `make -B mockr`
mockr: mockr/mockr.py
	@python -m mockr.mockr

readr: mockr/readr.py
	@python -m mockr.readr

mockr-check:
	@ruff check mockr/*.py

mockr-format:
	@ruff format mockr/*.py

# to build the mail server, see minimail/Makefile
minimail: minimail/minimail
	@./minimail/minimail
