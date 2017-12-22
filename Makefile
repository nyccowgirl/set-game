default: browserify
setup: pip-install npm-install browserify
browserify: static/js/bundle.js
npm-install: 
	npm install
pip-install:
	pip install -r requirements.txt
static/js/bundle.js: static/js/is_set.js 
	./node_modules/.bin/browserify static/js/is_set.js -o static/js/bundle.js
	