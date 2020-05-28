function test(){
    const factsForm = document.querySelector('#facts-form'); // Селектор формы фактов

    let correctAnswers = 0;
    let arrayOfResults = []; // Массив, где будут храниться все значения
    const proverka = () => {
        const selector = '#facts-form input[type=radio]'; // селектор инпутов с типом радио внутри формы
        document.querySelectorAll(selector)  //сюда кидаем этот селектор, он вернет массив, по котором мы пробегаем методом foreach не мутирая его
        .forEach(el => {  //выбираем текущий элемент
            if (el.checked) { //если у элемента флаг checked === true
                arrayOfResults.push(el.value) //добавляем значение элемента в массив всех значений
            }
        })
    }

    // добавляем обработчик на отправку форм
    factsForm.addEventListener("submit", e => {
        e.preventDefault(); // сбрасываем действие по умолчанию
        //console.log('Не стоит вскрывать этот код, вы молодые, шутливые');
        proverka() // вызываем проверку которая добавит все значения в массив
        if (arrayOfResults.length < 5) return alert('Необходимо выбрать все ответы')
            else for (let i=0; i<5; i++) {
                if (arrayOfResults[i] == 1) correctAnswers++;
            }
        //return alert("Правильных ответов : " + correctAnswers + ' Выбранные значения: ' + arrayOfResults) // выведем все значения в консоль
        document.getElementById('rezult').innerHTML = ('Правильных ответов: ' + correctAnswers)
        arrayOfResults = [];
    });
}

