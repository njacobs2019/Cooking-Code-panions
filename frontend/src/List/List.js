import React from "react";
import ListItem from "./ListItem";
import ListControl from "./ListControl";


function List(props){
    const [listItems, setListItems] = React.useState([
        {
            id: 1,
            text: "List item 1"
        },
        {
            id: 2,
            text: "List item 2"
        },
        {
            id: 3,
            text: "List item 3"
        },
    ]);

    const addItem = (text) => {
        var newItem = {id: listItems.length+1, text:text}
        var newArray = [...listItems]
        newArray.push(newItem)
        setListItems(newArray)
    };

    const removeItem = (id) => {
        var newArray = [...listItems].filter((item) => item.id !== id)
        setListItems(newArray)
    };

    return(
      <div>
        <ul>
            {listItems.map(item => (
                <ListItem
                    key = {item.id}
                    id = {item.id}
                    text = {item.text}
                    removeItem = {removeItem}
                    />
                ))}
        </ul>
        <ListControl addItem={addItem} />
      </div>
    );
}
export default List;