let book = [
    {
        id: 0,
        description: "Du vaknar upp i ett rum. Du ser en dörr och ett fönster.",
        choices: [
            {
                description: "Gå till dörren",
                target: 1
            },
            {
                description: "Ät ost", target: 2
            }
        ]
    },
    {
        id: 1,
        description: "Du går till dörren.",
        choices: [
            {
                description: "You ded", target: null
            }

        ]
    },
    {
        id: 2,
        description: "Du äter ost tills du spricker",
        choices: [

        ]

    }
]

function findPage(id) {
    return book.find((page) => {
        return page.id === id;
    })
}


function presentPage(page) {
    console.log(page.description);
    page.choices.forEach((choice) => {
        console.log(choice.description);
    })
}


page = 0

while (page !== null) {
    console.log(page)
    let currentPage = findPage(page);
    console.log(currentPage)
    presentPage(currentPage);
    page = prompt("Vad väljer du? ");
}