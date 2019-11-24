(this["webpackJsonpmoney-visualizer"]=this["webpackJsonpmoney-visualizer"]||[]).push([[0],{167:function(e,t,a){e.exports=a(356)},172:function(e,t,a){},173:function(e,t,a){},354:function(e,t,a){},355:function(e,t,a){},356:function(e,t,a){"use strict";a.r(t);var n=a(1),r=a.n(n),l=a(47),i=a.n(l),s=a(126),c=a(127),u=a(138),o=a(128),m=a(139);a(172);var p=function(e){return r.a.createElement("div",{className:"typeswitcher-container"},r.a.createElement("button",{value:"investment",onClick:e.changeCurrentView,className:"investment"===e.currentView?"typeswitcher-button-pressed":{}},"INVESTMENT"),r.a.createElement("button",{value:"debt",onClick:e.changeCurrentView,className:"debt"===e.currentView?"typeswitcher-button-pressed":{}},"DEBT"))};a(173);var h=function(e){var t=r.a.createElement("div",{className:"inputvalues-container"},r.a.createElement("div",{className:"inputvalues-item"},r.a.createElement("h1",null,"Starting Amount:"),r.a.createElement("span",{className:"inputvalues-input"},"$",r.a.createElement("input",{value:e.amount,onChange:e.changeAmount,placeholder:"Required"}))),r.a.createElement("div",{className:"inputvalues-item"},r.a.createElement("h1",null,"Monthly Contributions:"),r.a.createElement("span",{className:"inputvalues-input"},"$",r.a.createElement("input",{value:e.payment,onChange:e.changePayment,placeholder:"Required"}))),r.a.createElement("div",{className:"inputvalues-item"},r.a.createElement("h1",null,"Annual Rate of Return:"),r.a.createElement("span",{className:"inputvalues-input"},"%",r.a.createElement("input",{value:e.rate,onChange:e.changeRate,placeholder:"Required"}))),r.a.createElement("div",{className:"inputvalues-item"},r.a.createElement("h1",null,"Years to Grow:"),r.a.createElement("span",{className:"inputvalues-input"},"#",r.a.createElement("input",{value:e.years,onChange:e.changeYears,placeholder:"Required"})))),a=r.a.createElement("div",{className:"inputvalues-container"},r.a.createElement("div",{className:"inputvalues-item"},r.a.createElement("h1",null,"Debt Amount:"),r.a.createElement("span",{className:"inputvalues-input"},"$",r.a.createElement("input",{value:e.amount,onChange:e.changeAmount,placeholder:"Required"}))),r.a.createElement("div",{className:"inputvalues-item"},r.a.createElement("h1",null,"Monthly Payment:"),r.a.createElement("span",{className:"inputvalues-input"},"$",r.a.createElement("input",{value:e.payment,onChange:e.changePayment,placeholder:"Required"}))),r.a.createElement("div",{className:"inputvalues-item"},r.a.createElement("h1",null,"Annual Percentage Rate:"),r.a.createElement("span",{className:"inputvalues-input"},"%",r.a.createElement("input",{value:e.rate,onChange:e.changeRate,placeholder:"Required"}))));return r.a.createElement(r.a.Fragment,null,"investment"===e.currentView?t:a)},v=a(12);a(354);var d=function(e){var t=[],a=(new Date).getFullYear(),n=0,l=0;""!==e.years&&(l=parseInt(e.years));var i=0;""!==e.rate&&(i=parseInt(e.rate)/100);var s=0;""!==e.payment&&(s=parseInt(e.payment.split(",").join("")));var c=0;if(""!==e.amount&&(c=parseInt(e.amount.split(",").join(""))),"investment"===e.currentView){var u=c,o=c;t.push({Year:a,Total:o,Contributions:u,Interest:o-u});for(var m=1;m<=l;m++){for(var p=0;p<12;p++)o=o*(1+i/12)+s,u+=s;var h=Math.round(o).toFixed(0);t.push({Year:a+m,Total:h,Contributions:u,Interest:h-u})}}if("debt"===e.currentView){var d=c,g=c,E=c,y=i/12;for(t.push({Year:a,Total:d,Principal:E,Interest:d-E});d<g||l<=10;){if(d>=g&&10===l){l=-1;break}g=d;for(var f=0;f<12;f++)n+=d*y,d*=1+y,d-=s,E-=s;a+=1,l+=1;var w=Math.round(d).toFixed(0);if(E<0){if(!(d>0)){t.push({Year:a,Total:0,Principal:0,Interest:0});break}t.push({Year:a,Total:w,Principal:0,Interest:w-0})}else t.push({Year:a,Total:w,Principal:E,Interest:w-E})}}var b=r.a.createElement("p",null,"Your investment will be worth $",parseInt(t[t.length-1].Total).toLocaleString()," in ",l," years."),C=-1===l?r.a.createElement("p",null,"Your debt will increase indefinitely. Increase your monthly payment."):1===l?parseInt(n)>=0?r.a.createElement("p",null,"You will payoff your debt within 1 year, with $",parseInt(n.toFixed(0)).toLocaleString()," paid in interest."):r.a.createElement("p",null,"You will payoff your debt within 1 year, with no interest paid."):parseInt(n)>=0?r.a.createElement("p",null,"You will payoff your debt in ",l," years, with $",parseInt(n.toFixed(0)).toLocaleString()," paid in interest."):r.a.createElement("p",null,"You will payoff your debt in ",l," years, with no interest paid.");return r.a.createElement("div",{className:"charts-container"},"investment"===e.currentView?b:C,r.a.createElement(v.d,null,r.a.createElement(v.b,{data:t,margin:{top:20,right:20,left:20,bottom:20}},r.a.createElement(v.c,{strokeDasharray:"3 3"}),r.a.createElement(v.f,{dataKey:"Year"}),r.a.createElement(v.g,null),r.a.createElement(v.e,{content:r.a.createElement((function(e){var t=e.active,a=e.payload,n=e.label;return t?r.a.createElement("div",{className:"charts-custom-tooltip"},r.a.createElement("p",{className:"charts-label"},"".concat(n)),r.a.createElement("p",{className:"charts-label-total"},"Total : $".concat(parseInt(a[0].value+a[1].value).toLocaleString())),r.a.createElement("p",{className:"charts-label-interest"},"".concat(a[1].name," : $").concat(parseInt(a[1].value).toLocaleString())),r.a.createElement("p",{className:"charts-label-contributions"},"".concat(a[0].name," : $").concat(parseInt(a[0].value).toLocaleString()))):null}),null)}),r.a.createElement(v.a,{type:"monotone",dataKey:"investment"===e.currentView?"Contributions":"Principal",stackId:"1",stroke:"#82ca9d",fill:"#82ca9d"}),r.a.createElement(v.a,{type:"monotone",dataKey:"Interest",stackId:"1",stroke:"#ffc658",fill:"#ffc658"}))))};a(355);var g=function(e){var t=r.a.createElement(r.a.Fragment,null,r.a.createElement("h2",null,"Investment Calculator"),r.a.createElement("p",null,"This calculator will give a visual representation of how invested money can grow. The goal of this chart is to encourage people to think long term and to take advantage of compound interest. Visit our various articles to learn more.")),a=r.a.createElement(r.a.Fragment,null,r.a.createElement("h2",null,"Debt Repayment Calculator"),r.a.createElement("p",null,"This calculator will give a visual representation of how debt can grow. The goal of this chart is to encourage people to quickly pay off debt, and to encur less of it."));return r.a.createElement("div",{className:"description-container"},"investment"===e.currentView?t:a)},E=function(e){function t(e){var a;return Object(s.a)(this,t),(a=Object(u.a)(this,Object(o.a)(t).call(this,e))).handleCurrentViewChange=function(e){"investment"===e.target.value?a.setState(a.baseState):"debt"===e.target.value&&a.setState({currentView:"debt",amount:"5,000",payment:"100",rate:"16",years:"0"})},a.handleAmountChange=function(e){var t=e.target.value.split(",").join("").split(" ").join("");""!==t&&(t=parseInt(t)),(""===t||/^\d+$/.test(t)&&t<=1e7)&&(/^0+\d/.test(t)&&(t=t.substr(1)),a.setState({amount:t.toLocaleString()}))},a.handlePaymentChange=function(e){var t=e.target.value.split(",").join("").split(" ").join("");""!==t&&(t=parseInt(t)),(""===t||/^\d+$/.test(t)&&t<=1e6)&&(/^0+\d/.test(t)&&(t=t.substr(1)),a.setState({payment:t.toLocaleString()}))},a.handleRateChange=function(e){var t=e.target.value.includes(".")?e.target.value.split(".")[1].length:0;if(""===e.target.value||"."===e.target.value||!isNaN(e.target.value)&&e.target.value<=100&&t<=2){var n=e.target.value;/^0+\d/.test(e.target.value)&&(n=n.substr(1)),/^\./.test(e.target.value)&&(n="0."),a.setState({rate:n.split(" ").join("")})}},a.handleYearsChange=function(e){if(""===e.target.value||/^\d+$/.test(e.target.value)&&e.target.value<=100){var t=e.target.value;/^0+\d/.test(e.target.value)&&(t=t.substr(1)),a.setState({years:t.split(" ").join("")})}},a.state={currentView:"investment",amount:"1,000",payment:"100",rate:"8",years:"20"},a.baseState=a.state,a}return Object(m.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return r.a.createElement(r.a.Fragment,null,r.a.createElement(p,{currentView:this.state.currentView,changeCurrentView:this.handleCurrentViewChange}),r.a.createElement(h,{currentView:this.state.currentView,amount:this.state.amount,payment:this.state.payment,rate:this.state.rate,years:this.state.years,changeAmount:this.handleAmountChange,changePayment:this.handlePaymentChange,changeRate:this.handleRateChange,changeYears:this.handleYearsChange}),r.a.createElement(d,{currentView:this.state.currentView,amount:this.state.amount,payment:this.state.payment,rate:this.state.rate,years:this.state.years}),r.a.createElement(g,{currentView:this.state.currentView}))}}]),t}(r.a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(r.a.createElement(E,null),document.getElementById("money-visualizer-root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[167,1,2]]]);
//# sourceMappingURL=main.cf56e1cb.chunk.js.map