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
var maxTime = 3000;
var time_counter = 0;
var delay = 50;

function convertOptionsCidadesFromAPI(cidades) {
    let options = [];

    cidades.forEach(cidade => {
        options.push({
            label: cidade.nome,
            value: cidade.nome
        })
    });
    return options;
}

class SelectEstado extends React.Component {

    constructor(props) {
        super(props);
        this.selectCidadeRef = props.selectCidadeRef;
        this.state = {
            idSelect: props.idSelectEstado
        }
    }

    onchangeEstado = (option) => {

        let nomeCidadePadrao = "a"

        linkRoot = "/api/" + option.value + "/cidades/" + nomeCidadePadrao + "?limit=20";

        var cidades = []
        //variável para acessar o select
        //dentro da função done o this muda
        var this_ = this;
        $.get(linkRoot)
            .done(function (response) {
                cidades = convertOptionsCidadesFromAPI(response);
            });

        var interval = setInterval(function () {
            if (cidades.length > 0) {
                this_.selectCidadeRef.current.updateOptions(cidades);
                this_.selectCidadeRef.current.updateEstado(option.value);
                clearInterval(interval);
            }
            if (time_counter > maxTime) {
                clearInterval(interval);
            }
            time_counter += delay;
        }, delay);
    }

    render() {
        return <Select
            id={this.state.idSelect}
            onChange={this.onchangeEstado}
            options={
                estadoOptions
            }
            placeholder={"Digite o nome do estado"}
        />;
    }
}

class SelectCidade extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            options: [],
            estado: "",
            idSelect: props.idSelectCidade
        }
    }

    onInputChange = inputText => {

        linkRoot = "/api/" + this.state.estado + "/cidades/" + inputText + "?limit=20";

        var cidades = []
        //variável para acessar o select
        //dentro da função done o this muda
        var this_ = this;

        if (inputText.length < 2 || this.state.estado == "") {
            return
        }
        console.log(linkRoot);

        $.get(linkRoot)
            .done(function (response) {
                cidades = convertOptionsCidadesFromAPI(response);
            });

        var interval = setInterval(function () {
            if (cidades.length > 0) {
                this_.updateOptions(cidades);
                time_counter = 0;
                clearInterval(interval);
            }
            if (time_counter > maxTime) {
                time_counter = 0;
                clearInterval(interval);
                time_counter = 0;
            }
            time_counter += delay;
        }, delay);
    };

    onChange(option) {
        $("#input-cidade").val(option.label);
    }

    updateOptions(options) {
        this.setState({
            options: options
        });
    }

    updateEstado(estado) {
        this.state.estado = estado;
        $("#input-estado").val(estado);
    }

    render() {
        return <Select
            id={this.state.idSelect}
            onInputChange={this.onInputChange}
            onChange={this.onChange}
            options={this.state.options}
            placeholder={"Digite o nome da cidade"}
            noOptionsMessage={() => 'Selecione o estado e digite o nome da cidade'}
        />;
    }
}

class SelectWrapper extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            idSelectCidade: props.idSelectCidade,
            idSelectEstado: props.idSelectEstado
        };
        this.selectCidadeRef = React.createRef();
    }

    render() {
        return (
            <div>
                <input type="text" required hidden name="endereco-0-cidade" id="input-cidade"/>
                <input type="text" required hidden name="estado" id="input-estado"/>
                <div className="container">
                    <div className="row">
                        <div className="col-sm-12 col-md-12 col-lg-8">
                            <label>Selecione a cidade</label>
                            <SelectCidade idSelectCidade={this.props.idSelectCidade} ref={this.selectCidadeRef}/>
                        </div>
                        <div className="col-sm-12 col-md-12 col-lg-4">
                            <label>Selecione o Estado</label>
                            <SelectEstado idSelectEstado={this.props.idSelectEstado}
                                          selectCidadeRef={this.selectCidadeRef}/>
                        </div>
                    </div>
                </div>

            </div>
        )
    }
}


ReactDOM.render(<SelectWrapper
        idSelectCidade={"select-cidade"}
        idSelectEstado={"select-estado"}
    />,
    document.getElementById('form-busca')
);
