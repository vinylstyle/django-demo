
import React from "react"

class App extends React.Component {
  render() {
    const { name } = this.props

    return <h1 className="text-center text-4xl">Hello {name}!</h1>
  }
}

export default App
