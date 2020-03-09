var
  board = '',
  size = prompt("Pick board size");
for (var i = 0 ; i < size ; i++)
  {
    for(var j = 0 ; j < size ; j++)
    {
      board += (j % 2) == (i % 2) ? " " : "#";
    }
    board += "\n";
  }
