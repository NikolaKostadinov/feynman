const SideBarDiv = ({ srcPath, id, alt, text }) => {
    return (
        <div className="sideBarDiv" id={id}>
          <div>
            <img src={require(`../images/${srcPath}`)} alt={alt} width='300' height="300"/>
            <p>{text}</p>
          </div>
        </div>
    )
}

export default SideBarDiv