
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

var usuarioNome = document.getElementById("usuario-nome").value;
var usuarioTelefone = document.getElementById("usuario-telefone").value;
var usuarioEmail = document.getElementById("usuario-email").value;

function mensagemTipo2(){
    if (usuarioEmail == ""){
        return alert("Função disponível somente para usuários logados");
    }
    let mens = "Olá :D, bom dia! Me chamo " + usuarioNome +", e gostaria de mais informações sobre seu imóvel.\n\nPor favor, entrar em contato comigo: " + usuarioTelefone + " - " + usuarioEmail;
    document.getElementById("textarea-mens").value = mens;
}
function mensagemTipo1(){
    if (usuarioEmail == ""){
        return alert("Função disponível somente para usuários logados");
    }
    let mens = "Olá, me chamo " + usuarioNome +" e me interessei pelo seu imóvel. Estou entrando em contato em breve!";
    document.getElementById("textarea-mens").value = mens;
}

function mensagemTipo3(){
    if (usuarioEmail == ""){
        return alert("Função disponível somente para usuários logados");
    }
    let mens = "Bom dia! Meu nome é " + usuarioNome +", gostei bastante do seu imóvel, poderia entrar em contato comigo para mais informações?\n\nContato: " + usuarioTelefone + " - " + usuarioEmail;
    document.getElementById("textarea-mens").value = mens;
}

$(window).ready(function(){
    handleImgList();
    window.onresize = handleImgList;
})