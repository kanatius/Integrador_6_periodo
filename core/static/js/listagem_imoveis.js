var nextId = 50;

var estado = document.getElementById("estado").value.toString();
var cidade = document.getElementById("cidade").value.toString();

//link root para a chamada para carregar os imóveis disponíveis na cidade
var linkRoot = "/api/imoveis/" + estado + "/" + cidade

//carrega os primeiros dados da página
$(window).ready(function(){
    document.getElementById("carregar-mais").click();
});


class ListaImoveis extends React.Component {

    constructor(props) {
        super(props);
        
        this.state = {
            imoveis: [],
            carregando : false,
            qtdImoveisPorVez : 1,
            carregouTodos : false,
            msgDivFinal : ""
        };
    }

    getCard = (imovel) => {

        console.log(imovel);

        let urlImagem = (imovel.imagens.length == 0) ? "" : imovel.imagens[0].link;
        console.log(urlImagem);
        return (
            <div key={imovel.id} className="card col-lg-7">
                <div className="card-img">
                    <img src={urlImagem} className="card-img-top" alt="..." />
                </div>
                <div className="card-body">
                    <h5 className="card-title"><b>{imovel.tipo}</b></h5>
                    <p className="card-text"><b>{imovel.endereco.logradouro}, Nº {imovel.endereco.numero} - Bairro: {imovel.endereco.bairro}</b></p>
                    <p className="card-text">{imovel.descricao}</p>
                </div>
                <div className="card-footer">
                    <small className="text-muted"><a href="#">Detalhes</a></small>
                </div>
            </div>);
    }

    carregarMais() {

        //proibe que se faça mais de uma requisição por vez, pra evitar carregar dados iguais
        //Se carregou todos os imóveis não solicita mais
        if (this.state.carregando || this.state.carregouTodos){
            return
        }
        //modifica o status de chamada pra true
        this.state.carregando = true;

        //backup para acesso dentro da chamada ajax
        let _this = this;

        //offset sempre será o valor dos imóveis já carregados
        let offset = this.state.imoveis.length

        this.setState({
            msgDivFinal : "Carregando"
        });

        $.get(linkRoot + "?offset="+ offset +"&limit=" + this.state.qtdImoveisPorVez).done(function(imoveis){
            
            //adiciona os imóveis carregados
            _this.state.imoveis.push(...imoveis);

            _this.setState({
                msgDivFinal : ""
            });

            if(imoveis.length < _this.state.qtdImoveisPorVez){
                //se a quantidade de imoveis retornados for menor que a quantidade solicitada
                //define como true
                _this.state.carregouTodos = true;
                _this.setState({
                    msgDivFinal : "Não há mais imóveis disponíveis para locação na cidade de " + cidade + "-" + estado
                });

                if (_this.state.imoveis.length == 0){
                    _this.setState({
                        msgDivFinal : "Não há imóveis disponíveis para locação na cidade de " + cidade + "-" + estado
                    });
                }
            }

            _this.setState({imoveis: _this.state.imoveis});

            _this.state.carregando = false;
        });
    }

    render() {
        return (
            <div id="div-cards" className="row">
                {this.state.imoveis.map(this.getCard)}
                <button id="carregar-mais" className="btn" hidden onClick={this.carregarMais.bind(this)}>Carregar mais</button>
                <div style={ { "text-align" : "center" } }>
                    <br/>
                    {this.state.msgDivFinal}
                </div>
                <div></div>
            </div>
        );
    }
}

var listaIMoveis = React.createElement(ListaImoveis);

$(window).scroll(function () {
    if ($(window).scrollTop() >= $(document).height() - $(window).height() - 400) {
        document.getElementById("carregar-mais").click();
    }
});

ReactDOM.render(<ListaImoveis />, document.getElementById("imoveis-list"));