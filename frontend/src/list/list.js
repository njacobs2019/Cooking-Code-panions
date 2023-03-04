//Imports
import React from "react";

// list component from lab
function List(props)
{
    // state hook - essentially var declaration
    const [ListItems, setListItems] = React.useState([
        {
            id: 1,
            text: "user input 1"
        },
        {
            id: 2,
            text: "user input 2"
        },
        {
            id: 3,
            text: "user input 3"
        },
        
    ]);

    return(
        <ul>
            {ListItems.map[item => (
                <li>(item.text)</li>
            )]}
        </ul>
    );
}
export default List;