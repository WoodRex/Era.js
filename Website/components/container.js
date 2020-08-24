function Container(props) {
    React.useEffect(() => {
        let el = document.querySelector('.container')
        el.scrollTop = el.scrollHeight
    })
    let pages = []
    for (let i = 0; i < props.children.length; i++) {
        const el = props.children[i];
        if (i < props.children.length - 1) {
            el.disabled = true
            pages.push(Page(el))
        } else {
            pages.push(Page(el))
        }
    }
    return (
        React.createElement(
            'div',
            { className: 'container' },
            pages
        )
    );
}
function Page(props) {
    let blocks = []
    for (let i = 0; i < props.children.length; i++) {
        const el = props.children[i];
        if (props.hasOwnProperty('disabled') && props.disabled) {
            el.disabled = true
        }
        blocks.push(Block(el))
    }
    if (props.hasOwnProperty('disabled') && props.disabled) {
        return (
            React.createElement(
                'div',
                { className: 'page disabled' },
                blocks
            )
        )
    } else {
        return (
            React.createElement(
                'div',
                { className: 'page' },
                blocks
            )
        )
    }

}