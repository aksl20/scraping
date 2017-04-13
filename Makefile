clean:
	@pyclean .
	@rm -fr dist
	@rm -fr build
	@rm -fr scraping-*.dist-info
	@rm -fr scraping.egg-info
	@rm -fr */__pycache__
	@rm -fr __pycache__

requirements:
	@pip install -r requirements.txt

psi:
	@pip install . -U

wheel:
	@python setup.py bdist_wheel  # --universal if you are python2&3

test:
	@python setup.py test -q

python_count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
                      '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
