// describe("Test head of page", () => {
//     it("contains the correct title", () => {
//         cy.visit("http://localhost:3000/example-1"),

//         cy.get("h1") //grab h1 of our page.
//             .invoke("text")
//             // .should("equal", "Kura101") failed test
//             .should("equal", "My Awesome Web Application") 
//     });
// });


// describe("Testing input", () => {
//     it("check input number", () => {
//         cy.visit("http://localhost:3000/example-2"),

//         cy.get("span") //grab span of our page.
//             .invoke("text")
//             .should("equal", "15") 

//         cy.get("input").type("enter") //grab input and type
//         cy.get("span") //grab span that has the number of character.
//             .invoke("text")
//             .should("equal", "10") 
        
//     });
// });


describe("Testing input", () => {
    it("check input number", () => {
        cy.visit("http://localhost:3000/example-4"),

        cy.get('.jiqlbg > p > span:first')
            .invoke("text")
            .should("equal", "Nothing selected") 
        
        cy.get('.jiqlbg > ul > li:first').dblclick()
        .invoke("text")
        .should("equal", "Option One") 

        cy.get('.jiqlbg > p > span:first')
        .invoke("text")
        .should("equal", "Option One") 
    });
});
