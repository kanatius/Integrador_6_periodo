
function zoomImage(src) {
    document.getElementById("img-zoom").src = src;
}

document.getElementsByClassName("img-mini")[0].onclick();


function handleImgList(){
    console.log(window.innerWidth);
    if (window.innerWidth < 576){
        $("#div-imgs-left").hide();
        $(".img-wrapper-in-line").show();
    }else{
        $("#div-imgs-left").show();
        $(".img-wrapper-in-line").hide();
    } 
}

$(window).ready(function(){
    handleImgList();
    window.onresize = handleImgList;
})