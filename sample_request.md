```graphql
query Boards{
  boards {
    edges {
      node {
        id
        title
        content
        createdAt
      }
    }
  }
}

query Board {
  board(id: "Qm9hcmRUeXBlOjI=") {
    id
    title
    content
    createdAt
  }
}

mutation UpdateBoard {
  updateBoard(id: "Qm9hcmRUeXBlOjI=", input: {title: "아오", content: "열바더"}) {
    board {
      id
      title
      content
    }
  }
}

mutation CreateBoard {
  createBoard(input: {title: "new2", content: "it is new222"}) {
    board {
      id
      title
      content
    }
  }
}
```