var nextId = 50;
const imoveisTeste = [
    {
        id: 1,
        tipo: "Apartamento",
        descricao: "Em ótimo estado",
        ponto_de_referencia: "Perto da UERN",
        logradouro: "5044 Brooke Knolls",
        imagemURL: "/static/casa.jpg"
    },
    {
        id: 2,
        tipo: "Apartamento",
        descricao: "Em ótimo estado",
        ponto_de_referencia: "Perto da UERN",
        logradouro: "Santa Rita",
        imagemURL: "/static/casa2.jpg"
    },
    {
        id: 3,
        tipo: "Casa",
        descricao: "Em ótimo estado",
        ponto_de_referencia: "Perto da UERN",
        logradouro: "Rua Boa Vista",
        imagemURL: "/static/casa.jpg"
    },
    {
        id: 4,
        tipo: "Apartamento",
        descricao: "Em ótimo estado",
        ponto_de_referencia: "Perto da UERN",
        logradouro: "4332 Leannon Motorway",
        imagemURL: "/static/casa2.jpg"
    }
    // {
    //     id: 5,
    //     tipo: "Casa",
    //     descricao: "Em ótimo estado",
    //     ponto_de_referencia: "Perto da UERN",
    //     logradouro: "5044 Brooke Knolls",
    //     imagemURL: "/static/casa.jpg"
    // },
    // {
    //     id: 6,
    //     tipo: "Casa",
    //     descricao: "Em ótimo estado",
    //     ponto_de_referencia: "Perto da UERN",
    //     logradouro: "5044 Brooke Knolls",
    //     imagemURL: "/static/casa.jpg"
    // },
    // {
    //     id: 7,
    //     tipo: "Apartamento",
    //     descricao: "Em ótimo estado",
    //     ponto_de_referencia: "Perto da UERN",
    //     logradouro: "5044 Brooke Knolls",
    //     imagemURL: "/static/casa2.jpg"
    // }
]

class ListaImoveis extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            cards: imoveisTeste
        }
    }

    getCard = (card) => {

        return (
            <div key={card.id} className="card col-lg-7">
                <div className="card-img">
                    <img src={card.imagemURL} className="card-img-top" alt="..." />
                </div>
                <div className="card-body">
                    <h5 className="card-title"><b>{card.tipo}</b></h5>
                    <p className="card-text"><b>{card.logradouro}</b></p>
                    <p className="card-text">{card.descricao}</p>
                </div>
                <div className="card-footer">
                    <small className="text-muted"><a href="#">Detalhes</a></small>
                </div>
            </div>);
    }

    carregarMais() {
        let imgURL = (nextId % 2 == 0) ? "/static/casa.jpg" : "/static/casa2.jpg";
        this.state.cards.push({
            id: nextId++,
            tipo: "Apartamento",
            descricao: "Em ótimo estado",
            ponto_de_referencia: "Perto da UERN",
            logradouro: "Santa Rita",
            imagemURL: imgURL
        });

        this.setState({
            cards: this.state.cards
        });
    }

    render() {
        return (
            <div id="div-cards" className="row">
                {this.state.cards.map(this.getCard)}
                <button id="carregar-mais" className="btn" hidden onClick={this.carregarMais.bind(this)}>Carregar mais</button>
            </div>
        );
    }
}

var listaIMoveis = React.createElement(ListaImoveis);

$(window).scroll(function () {
    if ($(window).scrollTop() >= $(document).height() - $(window).height() - 10) {
        document.getElementById("carregar-mais").click();
    }
});

ReactDOM.render(listaIMoveis, document.getElementById("imoveis-list"));