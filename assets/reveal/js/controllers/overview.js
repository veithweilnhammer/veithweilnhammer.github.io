import{SLIDES_SELECTOR}from"../utils/constants.js";import{extend,queryAll,transformElement}from"../utils/util.js";export default class Overview{constructor(e){this.Reveal=e,this.active=!1,this.onSlideClicked=this.onSlideClicked.bind(this)}activate(){if(this.Reveal.getConfig().overview&&!this.isActive()){this.active=!0,this.Reveal.getRevealElement().classList.add("overview"),this.Reveal.cancelAutoSlide(),this.Reveal.getSlidesElement().appendChild(this.Reveal.getBackgroundsElement()),queryAll(this.Reveal.getRevealElement(),SLIDES_SELECTOR).forEach(e=>{e.classList.contains("stack")||e.addEventListener("click",this.onSlideClicked,!0)});const e=70,t=this.Reveal.getComputedSlideSize();this.overviewSlideWidth=t.width+e,this.overviewSlideHeight=t.height+e,this.Reveal.getConfig().rtl&&(this.overviewSlideWidth=-this.overviewSlideWidth),this.Reveal.updateSlidesVisibility(),this.layout(),this.update(),this.Reveal.layout();const i=this.Reveal.getIndices();this.Reveal.dispatchEvent({type:"overviewshown",data:{indexh:i.h,indexv:i.v,currentSlide:this.Reveal.getCurrentSlide()}})}}layout(){this.Reveal.getHorizontalSlides().forEach((e,t)=>{e.setAttribute("data-index-h",t),transformElement(e,"translate3d("+t*this.overviewSlideWidth+"px, 0, 0)"),e.classList.contains("stack")&&queryAll(e,"section").forEach((e,i)=>{e.setAttribute("data-index-h",t),e.setAttribute("data-index-v",i),transformElement(e,"translate3d(0, "+i*this.overviewSlideHeight+"px, 0)")})}),Array.from(this.Reveal.getBackgroundsElement().childNodes).forEach((e,t)=>{transformElement(e,"translate3d("+t*this.overviewSlideWidth+"px, 0, 0)"),queryAll(e,".slide-background").forEach((e,t)=>{transformElement(e,"translate3d(0, "+t*this.overviewSlideHeight+"px, 0)")})})}update(){const e=Math.min(window.innerWidth,window.innerHeight),t=Math.max(e/5,150)/e,i=this.Reveal.getIndices();this.Reveal.transformSlides({overview:["scale("+t+")","translateX("+-i.h*this.overviewSlideWidth+"px)","translateY("+-i.v*this.overviewSlideHeight+"px)"].join(" ")})}deactivate(){if(this.Reveal.getConfig().overview){this.active=!1,this.Reveal.getRevealElement().classList.remove("overview"),this.Reveal.getRevealElement().classList.add("overview-deactivating"),setTimeout(()=>{this.Reveal.getRevealElement().classList.remove("overview-deactivating")},1),this.Reveal.getRevealElement().appendChild(this.Reveal.getBackgroundsElement()),queryAll(this.Reveal.getRevealElement(),SLIDES_SELECTOR).forEach(e=>{transformElement(e,""),e.removeEventListener("click",this.onSlideClicked,!0)}),queryAll(this.Reveal.getBackgroundsElement(),".slide-background").forEach(e=>{transformElement(e,"")}),this.Reveal.transformSlides({overview:""});const e=this.Reveal.getIndices();this.Reveal.slide(e.h,e.v),this.Reveal.layout(),this.Reveal.cueAutoSlide(),this.Reveal.dispatchEvent({type:"overviewhidden",data:{indexh:e.h,indexv:e.v,currentSlide:this.Reveal.getCurrentSlide()}})}}toggle(e){"boolean"==typeof e?e?this.activate():this.deactivate():this.isActive()?this.deactivate():this.activate()}isActive(){return this.active}onSlideClicked(e){if(this.isActive()){e.preventDefault();let t=e.target;for(;t&&!t.nodeName.match(/section/gi);)t=t.parentNode;if(t&&!t.classList.contains("disabled")&&(this.deactivate(),t.nodeName.match(/section/gi))){let e=parseInt(t.getAttribute("data-index-h"),10),i=parseInt(t.getAttribute("data-index-v"),10);this.Reveal.slide(e,i)}}}};