const SideBarDiv = ({ srcPath, id, alt, text }) => {
    return (
        <div className="sideBarDiv" id={id}>
          <div>
            <img src={require(`../images/${srcPath}`)} alt={alt} />
            <p>{text}</p>
          </div>
        </div>
    )
}

export default SideBarDiv
