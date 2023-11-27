# default to python3
ifeq ($(origin PYTHON), undefined)
	PYTHON := $(shell which python3 || which python || echo python3)
endif
export PYTHON

.PHONY: all
all: .venv/bin/activate
	.venv/bin/pip --disable-pip-version-check install wheel
	.venv/bin/pip --disable-pip-version-check install -r requirements.txt

.PHONY: clean
clean:
	rm -rf .venv/

.venv/bin/activate:
	$(PYTHON) -m venv .venv
