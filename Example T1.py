# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  #Task 1 - amended to valid input
  valid = False
  while not valid:
    TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
    TypeOfGame = TypeOfGame.upper()[0]
    if TypeOfGame in ["Y","N"]:
      valid = True
    else:
      print("Please enter Y or N")
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("{0:<5}{1}".format("","-"*25))
    print("R{0:<1}".format(RankNo),end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("{0:<5}{1}".format("","-"*25))
  print()
  print("{0:<6}{1:<3}{2:<3}{3:<3}{4:<3}{5:<3}{6:<3}{7:<3}{8:<3}".format("","F1","F2","F3","F4","F5","F6","F7","F8"))
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  #Task 2 - prevent moves outside the board area
  elif StartRank in [0,BOARDDIMENSION+1]:
    MoveIsLegal = False
  elif FinishRank in [0,BOARDDIMENSION+1]:
    MoveIsLegal = False
  elif StartFile in [0,BOARDDIMENSION+1]:
    MoveIsLegal = False
  elif FinishFile in [0,BOARDDIMENSION+1]:
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  #task 3 - validate moves
  valid = False
  while not valid:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if StartSquare // 10 > 0:
        valid = True
      else:
        print("Please provide both FILE and RANK for this move")
    except ValueError:
      print("Please provide both FILE and RANK for this move")
  valid = False
  while not valid:
    try:
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      if FinishSquare // 10 > 0:
        valid = True
      else:
        print("Please provide both FILE and RANK for this move")
    except ValueError:
      print("Please provide both FILE and RANK for this move")
  return StartSquare, FinishSquare

#task 4 - move confirmation
def ConfirmMove(StartSquare, FinishSquare):
  StartRank = StartSquare % 10
  StartFile = StartSquare // 10
  FinishRank = FinishSquare % 10
  FinishFile = FinishSquare // 10
  print()
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartRank,StartFile,FinishRank, FinishFile))
  valid = False
  while not valid:
    confirm = input("Confirm move (Yes/No): ")
    confirm = confirm.upper()[0]
    if confirm in ["Y","N"]:
      valid = True
  if confirm == "Y":
    print("Move confirmed")
  else:
    print("Move cancelled")
    valid = False
  return valid

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  #Task 6 - promotion message
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    OriginalColour, OriginalPiece = GetPieceName(Board[StartRank][StartFile])
    PromotedColour, PromotedPiece = GetPieceName(Board[FinishRank][FinishFile])
    print()
    print("{0} {1} promoted to {2}.".format(OriginalColour, OriginalPiece, PromotedPiece))
    print()
    Board[StartRank][StartFile] = "  "
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
  else:
    #Task 5 - indicate piece has been taken
    if Board[FinishRank][FinishFile] != "  ":
      print()
      TakeColour, TakePiece = GetPieceName(Board[StartRank][StartFile])
      TakenColour, TakenPiece = GetPieceName(Board[FinishRank][FinishFile])
      print("{0} {1} takes {2} {3}.".format(TakeColour, TakePiece, TakenColour, TakenPiece))
      print()
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "

#Task 7 - Check whether Sarrum is in check
def CheckValidBoardPosition(Rank, File):
  valid = False
  if 1 <= Rank <= BOARDDIMENSION and 1 <= File <= BOARDDIMENSION:
    valid = True
  return valid

#Task 7 - Check whether Sarrum is in check   
def CheckWithRedum(Board,FinishRank, FinishFile,WhoseTurn):
  #Redum can take diagonally FORWARD one space to LEFT and RIGHT
  if WhoseTurn == "W":
    Sarrum = "BS"
  elif WhoseTurn == "B":
    Sarrum = "WS"
  Check = False
  if WhoseTurn == "W":
    #diagonal left foward
    if CheckValidBoardPosition(FinishRank-1, FinishFile-1):
      if Board[FinishRank-1][FinishFile-1] == Sarrum:
        Check = True
    #diagonal right foward
    elif CheckValidBoardPosition(FinishRank-1,FinishFile+1):
      if Board[FinishRank-1][FinishFile+1] == Sarrum:
        Check = True
  elif WhoseTurn == "B":
    #diagonal left foward
    if CheckValidBoardPosition(FinishRank+1,FinishFile-1):
      if Board[FinishRank+1][FinishFile-1] == Sarrum:
        Check = True
    #diagonal right foward
    elif CheckValidBoardPosition(FinishRank+1,FinishFile+1):
      if Board[FinishRank+1][FinishFile+1] == Sarrum:
        Check = True    
  return Check

#Task 7 - Check whether Sarrum is in check
def CheckWithNabu(Board,FinishRank, FinishFile,WhoseTurn):
  #Nabu can take diagonally one space in any direction
  if WhoseTurn == "W":
    Sarrum = "BS"
  elif WhoseTurn == "B":
    Sarrum = "WS"
  Check = False
  #diagonal left foward
  if CheckValidBoardPosition(FinishRank-1,FinishFile-1):
    if Board[FinishRank-1][FinishFile-1] == Sarrum:
      Check = True
  #diagonal right foward
  elif CheckValidBoardPosition(FinishRank-1,FinishFile+1):
    if Board[FinishRank-1][FinishFile+1] == Sarrum:
      Check = True
  #diagonal left back
  elif CheckValidBoardPosition(FinishRank+1, FinishFile-1):
    if Board[FinishRank+1][FinishFile-1] == Sarrum:
      Check = True
  #diagonal right back
  elif CheckValidBoardPosition(FinishRank+1,FileFile+1):
    if Board[FinishRank+1][FinishFile+1] == Sarrum:
      Check = True
  return Check

#Task 7 - Check whether Sarrum is in check
def CheckWithMarzazPani(Board,FinishRank, FinishFile,WhoseTurn):
  #Marzaz Pani can take horizontally and vertically one space in any direction
  if WhoseTurn == "W":
    Sarrum = "BS"
  elif WhoseTurn == "B":
    Sarrum = "WS"
  Check = False
  #foward one vertical
  if CheckValidBoardPosition(FinishRank-1,FinishFile):
    if Board[FinishRank-1][FinishFile] == Sarrum:
      Check = True
  #back one vertical
  elif CheckValidBoardPosition(FinishRank+1, FinishFile):
    if Board[FinishRank+1][FinishFile] == Sarrum:
      Check = True
  #left one horizontal
  elif CheckValidBoardPosition(FinishRank,FinishFile-1):
    if Board[FinishRank][FinishFile-1] == Sarrum:
      Check = True
  #right one horizontal
  elif CheckValidBoardPosition(FinishRank, FinishFile):
    if Board[FinishRank][FinishFile+1] == Sarrum:
      Check = True
  return Check

#Task 7 - Check whether Sarrum is in check
def CheckWithEtlu(Board,FinishRank, FinishFile,WhoseTurn):
  #Etlu can take horizontally and vertically two spaces in any direction
  if WhoseTurn == "W":
    Sarrum = "BS"
  elif WhoseTurn == "B":
    Sarrum = "WS"
  Check = False
  #foward two vertical
  if CheckValidBoardPosition(FinishRank-2,FinishFile):
    if Board[FinishRank-2][FinishFile] == Sarrum:
      Check = True
  #back two vertical
  elif CheckValidBoardPosition(FinishRank-2, FinishFile):
    if Board[FinishRank-2][FinishFile] == Sarrum:
      Check = True
  #left two horizontal
  elif CheckValidBoardPosition(FinishRank, FinishFile-2):
    if Board[FinishRank][FinishFile-2] == Sarrum:
      Check = True
  #right two horizontal
  elif CheckValidBoardPosition(FinishRank,FinishFile+2):
    if Board[FinishRank][FinishFile+2] == Sarrum:
      Check = True
  return Check

#Task 7 - Check whether Sarrum is in check
def CheckWithGisgigir(Board,FinishRank, FinishFile,WhoseTurn):
  #Gisgigir can take horizontally and vertically any number of spaces in any direction
  if WhoseTurn == "W":
    Sarrum = "BS"
  elif WhoseTurn == "B":
    Sarrum = "WS"
  Check = False
  #check forward
  blocked = False
  for rank in range(FinishRank+1,BOARDDIMENSION+1):
    if CheckValidBoardPosition(rank,FinishFile):
      if Board[rank][FinishFile] == Sarrum and not blocked:
        Check = True
      elif Board[rank][FinishFile] != "  ":
        blocked = True
  #check backwards
  if not Check:
    blocked = False
    for rank in range(1,FinishRank):
      if CheckValidBoardPosition(rank,FinishFile):
        if Board[rank][FinishFile] == Sarrum and not blocked:
          Check = True
        elif Board[rank][FinishFile] != "  ":
          blocked = True
  #check right
  if not Check:
    blocked = False
    for file in range(FinishFile+1, BOARDDIMENSION+1):
      if CheckValidBoardPosition(FinishRank,file):
        if Board[FinishRank][file] == Sarrum and not blocked:
          Check = True
        elif Board[FinishRank][file] != "  ":
          blocked = True
  #check left
  if not Check:
    blocked = False
    for file in range(FinishFile-1, 1,-1):
      if CheckValidBoardPosition(FinishRank,file):
        if Board[FinishRank][file] == Sarrum and not blocked:
          Check = True
        elif Board[FinishRank][file] != "  ":
          blocked = True
  return Check

#Task 7 - Check whether Sarrum is in check
def CheckSarrumInCheck(Board,FinishRank, FinishFile,WhoseTurn):
  PieceCode = Board[FinishRank][FinishFile]
  Colour, Piece = GetPieceName(PieceCode)
  print(Colour,Piece)
  Check = False
  if Piece == "Marzaz Pani":
    Check = CheckWithMarzazPani(Board,FinishRank, FinishFile,WhoseTurn)
  elif Piece == "Nabu":
    Check = CheckWithNabu(Board,FinishRank, FinishFile,WhoseTurn)
  elif Piece == "Etlu":
    Check = CheckWithEtlu(Board,FinishRank, FinishFile,WhoseTurn)
  elif Piece == "Gisgigir":
    Check = CheckWithGisgigir(Board,FinishRank, FinishFile,WhoseTurn)
  elif Piece == "Redum":
    Check = CheckWithRedum(Board,FinishRank, FinishFile,WhoseTurn)
  return Check,PieceCode,FinishRank,FinishFile

#Task 7 - Check whether Sarrum is in check
def CheckMessage(PieceCode,FinishRank,FinishFile):
  Colour, Piece = GetPieceName(PieceCode)
  if Colour == "White":
    Sarrum = "Black"
  elif Colour == "Black":
    Sarrum = "White"
  print("{0} {1} in Rank {2}, File {3} has {4} Sarrum in Check.".format(Colour,Piece,FinishRank,FinishFile,Sarrum))
  

#Task 5 - new function (indicate piece has been taken)
def GetPieceName(PieceCode):
  Colour = PieceCode[0]
  Piece = PieceCode[1]
  if Colour == "W":
    Colour = "White"
  elif Colour == "B":
    Colour = "Black"
  if Piece == "S":
    Piece = "Sarrum"
  elif Piece == "M":
    Piece = "Marzaz Pani"
  elif Piece == "N":
    Piece = "Nabu"
  elif Piece == "E":
    Piece = "Etlu"
  elif Piece == "G":
    Piece = "Gisgigir"
  elif Piece == "R":
    Piece = "Redum"
  return Colour, Piece



    
if __name__ == "__main__":
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    #Task 1 - amend code to use GetTypeOfGame() function
    SampleGame = GetTypeOfGame()
    InitialiseBoard(Board, SampleGame)
    Check = False
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        Confirm = ConfirmMove(StartSquare, FinishSquare)
        if Confirm:
          StartRank = StartSquare % 10
          StartFile = StartSquare // 10
          FinishRank = FinishSquare % 10
          FinishFile = FinishSquare // 10
          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if Check:
            MoveSquareContents = Board[FinishRank][FinishFile]
          print()
          if not(MoveIsLegal):
            print("That is not a legal move - please try again")
          if MoveIsLegal:
            GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
            MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if MoveIsLegal and Check:
            Colour, Piece = GetPieceName(PieceCode)
            if WhoseTurn == "W":
              CheckTurn = "B"
            else:
              CheckTurn = "W"
            #check to see if check piece has been taken
            CheckPiece = Board[CheckRank][CheckFile]
            if CheckPiece == PieceCode:
              Check,PieceCode,CheckRank,CheckFile = CheckSarrumInCheck(Board,CheckRank, CheckFile,CheckTurn)
            else:
              Check = False
            #if still in check then move must be prevented
            if Check:
              print("Sarrum must be moved out of check from {0} {1} in Rank {2}, File {3}".format(Colour, Piece, CheckRank, CheckFile))
              MoveIsLegal = False
              #rewind move
              Board[StartRank][StartFile] = Board[FinishRank][FinishFile]
              Board[FinishRank][FinishFile] = MoveSquareContents
              print("Move cancelled")
          print()
      #GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      #MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)      
      Check,PieceCode,CheckRank,CheckFile = CheckSarrumInCheck(Board,FinishRank, FinishFile,WhoseTurn)
      print(Check)
      if Check:
        CheckMessage(PieceCode,CheckRank,CheckFile)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)
