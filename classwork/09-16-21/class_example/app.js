// // Created a variable
// let title = React.createElement(
//     "h1",
//     {},
//     "This is React"
// );

// let par = React.createElement(
//     "p",
//     {style: {backgroundColor: "red"}},
//     "This is a React in red"
// );

// let header = React.createElement(
//     "header",
//     {style: {backgroundColor: "red"}},
//     title,
//     par,
// );


// let footer = React.createElement(
//     "footer",
//     {style: {backgroundColor: "blue"}},
//     "This is a footer"
// );
// // create a head, footer. inside head and footer, put some text. 
// // when added, color the background of header.

// let main = React.createElement(
//     "main",
//     null,
//     header,
//     footer
// );


let title = <h1>This is React</h1>
let par = <p>This is another line</p>
var myID = "id"

var header = (
    <header>
        <h1> {title} </h1>
        <p id={myID}> {par} </p>
    </header>
)

ReactDOM.render(
    header,
    document.getElementById("root")
)