import React from "react"

function ListControl(props){
    const  [text, setText] = React.useState("");

    const onChange = e => {
        setText(e.target.value);
    }

    const handleSubmit = e => {
        e.preventDefault();
        props.addItem(text)
        setText("");
    }

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="text" value={text} onChange={onChange} />
            <input type="submit" value="Add item" />
        </form>
    );
}

export default ListControl;