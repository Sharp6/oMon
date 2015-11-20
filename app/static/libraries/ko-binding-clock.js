(function (factory) {
    // Module systems magic dance.

    if (typeof require === "function" && typeof exports === "object" && typeof module === "object") {
        // CommonJS or Node: hard-coded dependency on "knockout"
        factory(require("knockout", "jquery"));
    } else if (typeof define === "function" && define["amd"]) {
        // AMD anonymous module with hard-coded dependency on "knockout"
        define(["knockout", "jquery"], factory);
    } else {
        // <script> tag: use the global `ko` object, attaching a `mapping` property
        factory(ko,$);
    }
}
(function(ko,$) {
	ko.bindingHandlers.slider = {
	  init: function (element, valueAccessor, allBindingsAccessor) {
	    var options = allBindingsAccessor().sliderOptions || {};
	    $(element).slider(options);
	    ko.utils.registerEventHandler(element, "slidechange", function (event, ui) {
	        var observable = valueAccessor();
	        observable(ui.value);
	    });
	    ko.utils.domNodeDisposal.addDisposeCallback(element, function () {
	        $(element).slider("destroy");
	    });
	    ko.utils.registerEventHandler(element, "slide", function (event, ui) {
	        var observable = valueAccessor();
	        observable(ui.value);
	    });
	  },
	  update: function (element, valueAccessor) {
	    var value = ko.utils.unwrapObservable(valueAccessor());
	    if (isNaN(value)) value = 0;
	    $(element).slider("value", value);
	  }
	};
}));