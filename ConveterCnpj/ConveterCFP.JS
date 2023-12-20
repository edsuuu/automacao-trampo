const fs = require('fs');

function transformarTextoEmJSON() {

    const conteudoTxt = fs.readFileSync('seuarquivo.txt', 'utf-8');

    const linhas = conteudoTxt.split('\n');

    const numeros = linhas.map((linha) => linha.trim());

    const jsonDados = JSON.stringify(numeros, null, 2);

    fs.writeFileSync('dados.json', jsonDados, 'utf-8');
}

function formatarCnpj(numero) {
    const numeroString = numero.toString();
    const tamanho = numeroString.length;
    
    if (tamanho === 14) {
        return `${numeroString.slice(0, 2)}.${numeroString.slice(2, 5)}.${numeroString.slice(5, 8)}/${numeroString.slice(8, 12)}-${numeroString.slice(12, 14)}`;
    }
    
    if (tamanho === 11) {
        return `${numeroString.slice(0, 3)}.${numeroString.slice(3, 6)}.${numeroString.slice(6, 9)}-${numeroString.slice(9, 11)}`;
    }


    return numeroString;
}

transformarTextoEmJSON();

const dadosJson = fs.readFileSync('dados.json', 'utf-8');

const listaOriginalJson = JSON.parse(dadosJson);
const resultadosFormatados = listaOriginalJson.map(numero => formatarCnpj(numero));
const resultadosTxt = resultadosFormatados.join("\n");


fs.writeFileSync('resultados.txt', resultadosTxt, 'utf-8');

console.log('Finalizando');