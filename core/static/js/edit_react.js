

// -------- BTN ADICIONAR FOTO --------- //

$($(".img-field:hidden")[0]).removeAttr("hidden");

$("#add-item").on("click", function(){

    if($(".img-field:hidden").length == 0){
        return;
    }

    let imgFields = $(".img-field:hidden");

    let imgF = imgFields[0];

    let ffield = $(imgF).children("input")[0];

    // console.log(ffield);

    // if($(imgF).val()){ //aparece o file field caso tenha selecionado alguma imagem
    $(imgF).removeAttr('hidden');
    // }
    $(ffield).focus().trigger('click');
    if($(".img-field:hidden").length == 0){
        $(this).hide();
        return;
    }

});