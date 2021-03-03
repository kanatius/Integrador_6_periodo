const estadoOptions = [{
        value: "AC",
        label: "Acre"
    },
    {
        value: "AL",
        label: "Alagoas"
    },
    {
        value: "AP",
        label: "Amapá"
    },
    {
        value: "AM",
        label: "Amazonas"
    },
    {
        value: "BA",
        label: "Bahia"
    },
    {
        value: "CE",
        label: "Ceará"
    },
    {
        value: "DF",
        label: "Distrito Federal"
    },
    {
        value: "ES",
        label: "Espirito Santo"
    },
    {
        value: "GO",
        label: "Goiás"
    },
    {
        value: "MA",
        label: "Maranhão"
    },
    {
        value: "MS",
        label: "Mato Grosso do Sul"
    },
    {
        value: "MT",
        label: "Mato Grosso"
    },
    {
        value: "MG",
        label: "Minas Gerais"
    },
    {
        value: "PA",
        label: "Pará"
    },
    {
        value: "PB",
        label: "Paraíba"
    },
    {
        value: "PR",
        label: "Paraná"
    },
    {
        value: "PE",
        label: "Pernambuco"
    },
    {
        value: "PI",
        label: "Piauí"
    },
    {
        value: "RJ",
        label: "Rio de Janeiro"
    },
    {
        value: "RN",
        label: "Rio Grande do Norte"
    },
    {
        value: "RS",
        label: "Rio Grande do Sul"
    },
    {
        value: "RO",
        label: "Rondônia"
    },
    {
        value: "RR",
        label: "Roraima"
    },
    {
        value: "SC",
        label: "Santa Catarina"
    },
    {
        value: "SP",
        label: "São Paulo"
    },
    {
        value: "SE",
        label: "Sergipe"
    },
    {
        value: "TO",
        label: "Tocantins"
    }
];

var linkRoot = ""

class SelectEstado extends React.Component {

    constructor(props){
        super(props);
        this.selectCidadeRef = props.selectCidadeRef;
    }

    onchangeEstado = (option) => {

        linkRoot = "/api/" + option.value + "/cidades/a";
        
        var cidades = []
        //variável para acessar o select
        //dentro da função done o this muda
        var this_ = this;
        $.get(linkRoot)
            .done(function (response) {
                let options = [];

                response.forEach(cidade => {
                    options.push({
                        label : cidade.fields.nome,
                        value : cidade.fields.nome
                    })
                });
                cidades = options; 
        });

        var maxTime = 3000;
        var time_counter = 0;
        var delay = 50;

        var interval = setInterval(function(){
            if (cidades.length > 0){
                this_.selectCidadeRef.current.updateOptions(cidades);
                clearInterval(interval);
            }
            if(time_counter > maxTime){
                clearInterval(interval);
            }
            time_counter += delay;
        }, delay);
    }

    render() {
        return <Select onChange = {
            this.onchangeEstado
        }
        options = {
            estadoOptions
        }
        />;
    }
}

class SelectCidade extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            name : "select cidade",
            options : [{
                value: "askldmlas",
                label : "alksndkasn"
            }]
        }
    }

    printOptions = () => {
        console.log(this.state.options);
        console.log(this.state.name);
    }

    updateOptions(options){
        this.setState({options : options});
        console.log(this.state);
    }

    render() {
        return <Select onChange={this.printOptions} options={this.state.options} />;
    }
}

class SelectWrapper extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            cidadeOptions: [{
                label : "TESTE CIDADE",
                value : "asd"
            }]
        };
        this.selectCidadeRef = React.createRef();
    }

    render() {
        return (<div>
            <SelectEstado selectCidadeRef={this.selectCidadeRef} />
            <SelectCidade ref={this.selectCidadeRef}/>
        </div>)
    }
}


ReactDOM.render( <
    SelectWrapper / > ,
    document.getElementById('div-select')
);