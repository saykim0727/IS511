var injector = function(){
	if(arguments.length == 2) {
		var path = arguments[0];
		var cb = arguments[1];

		var script = document.createElement('script');
		
			script.src = chrome.extension.getURL(path);
		script.onload = function() {
			this.remove();
			if(cb !== undefined && typeof cb == 'function') {
				cb();
			}
		};
		
		(document.head||document.documentElement).appendChild(script);
	
	} else if (arguments.length == 1) {
		var text = arguments[0];

		var script = document.createElement('script');
		script.textContent = text;
		(document.head||document.documentElement).appendChild(script);
		
		script.remove();
	};
};

injector("js/customworker.js",null);
injector("js/wsHook.js",null);
