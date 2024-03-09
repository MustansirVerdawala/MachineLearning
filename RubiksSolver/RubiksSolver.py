from random import randint

#Building the cube

'''
ax1=White to Yellow
ax2=Red to Orange
ax3=Blue to Green
Position is of the form ax1, ax2, ax3
'''

#Each piece is of the form CurrentPosition, Orientation


WR={'Or':[1,2,0], 'CPos':[1,1,0]}
WB={'Or':[1,0,3], 'CPos':[1,0,1]}
WO={'Or':[1,-2,0], 'CPos':[1,-1,0]}
WG={'Or':[1,0,-3], 'CPos':[1,0,-1]}
RB={'Or':[0,2,3], 'CPos':[0,1,1]}
OB={'Or':[0,-2,3], 'CPos':[0,-1,1]}
OG={'Or':[0,-2,-3], 'CPos':[0,-1,-1]}
RG={'Or':[0,2,-3], 'CPos':[0,1,-1]}
YR={'Or':[-1,2,0], 'CPos':[-1,1,0]}
YB={'Or':[-1,0,3], 'CPos':[-1,0,1]}
YO={'Or':[-1,-2,0], 'CPos':[-1,-1,0]}
YG={'Or':[-1,0,-3], 'CPos':[-1,0,-1]}

WRB={'Or':[1,2,3], 'CPos':[1,1,1]}
WOB={'Or':[1,-2,3], 'CPos':[1,-1,1]}
WOG={'Or':[1,-2,-3], 'CPos':[1,-1,-1]}
WRG={'Or':[1,2,-3], 'CPos':[1,1,-1]}
YRB={'Or':[-1,2,3], 'CPos':[-1,1,1]}
YOB={'Or':[-1,-2,3], 'CPos':[-1,-1,1]}
YOG={'Or':[-1,-2,-3], 'CPos':[-1,-1,-1]}
YRG={'Or':[-1,2,-3], 'CPos':[-1,1,-1]}

corners = {'WRB':WRB, 'WOB':WOB, 'WOG':WOG, 'WRG':WRG, 'YRB':YRB, 'YOB':YOB, 'YOG':YOG, 'YRG':YRG}

edges={'WR':WR, 'WB':WB, 'WO':WO, 'WG':WG, 'RB':RB, 'OB':OB, 'OG':OG, 'RG':RG, 'YR':YR, 'YB':YB, 'YO':YO, 'YG':YG}

cube={'C':corners, 'E':edges}


#Defining Moves

def R(cube):

    corners, edges = cube['C'].copy(), cube['E'].copy()

    pieces=[corners['YRG'].copy(),corners['WRG'].copy(),corners['WOG'].copy(),corners['YOG'].copy(),corners['YRG'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      pieces[i]['Or']=[Or[1],Or[0],Or[2]]

    corners['YRG'],corners['WRG'],corners['WOG'],corners['YOG']=pieces[0:4]

    pieces=[edges['RG'].copy(),edges['WG'].copy(),edges['OG'].copy(),edges['YG'].copy(),edges['RG'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      if i%2==0:
        pieces[i]['Or']=[0,Or[0],Or[2]]
      else:
        pieces[i]['Or']=[Or[1],0,Or[2]]

    edges['RG'],edges['WG'],edges['OG'],edges['YG']=pieces[0:4]

    cube={'C':corners, 'E':edges}

    return cube

def RP(cube):
    return R(R(R(cube)))

def R2(cube):
    return R(R(cube))

def L(cube):

    corners, edges = cube['C'].copy(), cube['E'].copy()

    pieces=[corners['YRB'].copy(),corners['YOB'].copy(),corners['WOB'].copy(),corners['WRB'].copy(),corners['YRB'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      pieces[i]['Or']=[Or[1],Or[0],Or[2]]

    corners['YRB'],corners['YOB'],corners['WOB'],corners['WRB']=pieces[0:4]

    pieces=[edges['RB'].copy(),edges['YB'].copy(),edges['OB'].copy(),edges['WB'].copy(),edges['RB'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      if i%2==0:
        pieces[i]['Or']=[0,Or[0],Or[2]]
      else:
        pieces[i]['Or']=[Or[1],0,Or[2]]

    edges['RB'],edges['YB'],edges['OB'],edges['WB']=pieces[0:4]

    cube={'C':corners, 'E':edges}

    return cube

def LP(cube):
    return L(L(L(cube)))

def L2(cube):
    return L(L(cube))

def U(cube):

    corners, edges = cube['C'], cube['E']

    pieces=[corners['YRB'].copy(),corners['YRG'].copy(),corners['YOG'].copy(),corners['YOB'].copy(),corners['YRB'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      pieces[i]['Or']=[Or[0],Or[2],Or[1]]

    corners['YRB'],corners['YRG'],corners['YOG'],corners['YOB']=pieces[0:4]

    pieces=[edges['YR'].copy(),edges['YG'].copy(),edges['YO'].copy(),edges['YB'].copy(),edges['YR'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      if i%2==0:
        pieces[i]['Or']=[Or[0],Or[2],0]
      else:
        pieces[i]['Or']=[Or[0],0,Or[1]]

    edges['YR'],edges['YG'],edges['YO'],edges['YB']=pieces[0:4]

    cube={'C':corners, 'E':edges}

    return cube

def UP(cube):
    return U(U(U(cube)))

def U2(cube):
    return U(U(cube))

def D(cube):

    corners, edges = cube['C'], cube['E']

    pieces=[corners['WRB'].copy(),corners['WOB'].copy(),corners['WOG'].copy(),corners['WRG'].copy(),corners['WRB'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      pieces[i]['Or']=[Or[0],Or[2],Or[1]]

    corners['WRB'],corners['WOB'],corners['WOG'],corners['WRG']=pieces[0:4]

    pieces=[edges['WR'].copy(),edges['WB'].copy(),edges['WO'].copy(),edges['WG'].copy(),edges['WR'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      if i%2==0:
        pieces[i]['Or']=[Or[0],Or[2],0]
      else:
        pieces[i]['Or']=[Or[0],0,Or[1]]

    edges['WR'],edges['WB'],edges['WO'],edges['WG']=pieces[0:4]

    cube={'C':corners, 'E':edges}

    return cube

def DP(cube):
    return D(D(D(cube)))

def D2(cube):
    return D(D(cube))

def F(cube):

    corners, edges = cube['C'], cube['E']

    pieces=[corners['YRB'].copy(),corners['WRB'].copy(),corners['WRG'].copy(),corners['YRG'].copy(),corners['YRB'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      pieces[i]['Or']=[Or[2],Or[1],Or[0]]

    corners['YRB'],corners['WRB'],corners['WRG'],corners['YRG']=pieces[0:4]

    pieces=[edges['YR'].copy(),edges['RB'].copy(),edges['WR'].copy(),edges['RG'].copy(),edges['YR'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      if i%2==0:
        pieces[i]['Or']=[Or[2],Or[1],0]
      else:
        pieces[i]['Or']=[0,Or[1],Or[0]]

    edges['YR'],edges['RB'],edges['WR'],edges['RG']=pieces[0:4]

    cube={'C':corners, 'E':edges}

    return cube

def FP(cube):
    return F(F(F(cube)))

def F2(cube):
    return F(F(cube))

def B(cube):

    corners, edges = cube['C'], cube['E']

    pieces=[corners['YOG'].copy(),corners['WOG'].copy(),corners['WOB'].copy(),corners['YOB'].copy(),corners['YOG'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      pieces[i]['Or']=[Or[2],Or[1],Or[0]]

    corners['YOG'],corners['WOG'],corners['WOB'],corners['YOB']=pieces[0:4]

    pieces=[edges['YO'].copy(),edges['OG'].copy(),edges['WO'].copy(),edges['OB'].copy(),edges['YO'].copy()]

    for i in range(4):
      Or=pieces[i+1]['Or']
      if i%2==0:
        pieces[i]['Or']=[Or[2],Or[1],0]
      else:
        pieces[i]['Or']=[0,Or[1],Or[0]]

    edges['YO'],edges['OG'],edges['WO'],edges['OB']=pieces[0:4]

    cube={'C':corners, 'E':edges}

    return cube

def BP(cube):
    return B(B(B(cube)))

def B2(cube):
    return B(B(cube))

#Defining essential functions

def shuffleRandom(cube,num_moves=20):
    
    Moves=[]
    
    j=randint(1,18)
    
    Move=dict_num[j]
    cube=Move(cube)
    
    Moves.append(dict_num_alpha[j])
    
    j=randint(1,18)
    
    if num_moves>1:
        while True:
    
            if (dict_num_alpha[j][0]==Moves[0][0]):
                    j=randint(1,18)
            else:
                Move=dict_num[j]
                Moves.append(dict_num_alpha[j])
                cube=Move(cube)
                break
    
    for i in range(2,num_moves):

        j=randint(1,18)

        while True:
            
            flag=0

            for group in groups:
                if dict_num_alpha[j] in group:
                    if ((Moves[i-1] in group)) or ((Moves[i-2] in group)):
                        if (dict_num_alpha[j][0]==Moves[i-1][0]) or (dict_num_alpha[j][0]==Moves[i-2][0]):
                            j=randint(1,18)
                            break
                        else:
                            flag=1
                    else:
                        flag=1
            if flag:
                Move=dict_num[j]
                Moves.append(dict_num_alpha[j])
                cube=Move(cube)
                break
        
    return cube, Moves

def shuffleSeq(cube, s):

    Moves=[]

    s=s.split()

    for i in s:
        Move=dict_alpha[i]
        Moves.append(i)
        cube=Move(cube)

    return cube

def displayCube(cube):

  corners, edges = cube['C'], cube['E']

  print("\n\t\tCube Configuration\n******************************************************************************************************************")
  print("\n\n\tWhite Face\n")
  print('\n', corners['WRB']['Or'][0], edges['WR']['Or'][0], corners['WRG']['Or'][0])
  print('\n', edges['WB']['Or'][0], 1, edges['WG']['Or'][0])
  print('\n', corners['WOB']['Or'][0], edges['WO']['Or'][0], corners['WOG']['Or'][0])

  print("\n\n\tRed Face\n")
  print('\n', corners['YRB']['Or'][1], edges['YR']['Or'][1], corners['YRG']['Or'][1])
  print('\n', edges['RB']['Or'][1], 2, edges['RG']['Or'][1])
  print('\n', corners['WRB']['Or'][1], edges['WR']['Or'][1], corners['WRG']['Or'][1])

  print("\n\n\tGreen Face\n")
  print('\n', corners['YRG']['Or'][2], edges['YG']['Or'][2], corners['YOG']['Or'][2])
  print('\n', edges['RG']['Or'][2], -3, edges['OG']['Or'][2])
  print('\n', corners['WRG']['Or'][2], edges['WG']['Or'][2], corners['WOG']['Or'][2])

  print("\n\n\tOrange Face\n")
  print('\n', corners['YOG']['Or'][1], edges['YO']['Or'][1], corners['YOB']['Or'][1])
  print('\n', edges['OG']['Or'][1], -2, edges['OB']['Or'][1])
  print('\n', corners['WOG']['Or'][1], edges['WO']['Or'][1], corners['WOB']['Or'][1])

  print("\n\n\tBlue Face\n")
  print('\n', corners['YOB']['Or'][2], edges['YB']['Or'][2], corners['YRB']['Or'][2])
  print('\n', edges['OB']['Or'][2], 3, edges['RB']['Or'][2])
  print('\n', corners['WOB']['Or'][2], edges['WB']['Or'][2], corners['WRB']['Or'][2])

  print("\n\n\tYellow Face\n")
  print('\n', corners['YRG']['Or'][0], edges['YR']['Or'][0], corners['YRB']['Or'][0])
  print('\n', edges['YG']['Or'][0], -1, edges['YB']['Or'][0])
  print('\n', corners['YOG']['Or'][0], edges['YO']['Or'][0], corners['YOB']['Or'][0])

def reset():
  WR={'Or':[1,2,0], 'CPos':[1,1,0]}
  WB={'Or':[1,0,3], 'CPos':[1,0,1]}
  WO={'Or':[1,-2,0], 'CPos':[1,-1,0]}
  WG={'Or':[1,0,-3], 'CPos':[1,0,-1]}
  RB={'Or':[0,2,3], 'CPos':[0,1,1]}
  OB={'Or':[0,-2,3], 'CPos':[0,-1,1]}
  OG={'Or':[0,-2,-3], 'CPos':[0,-1,-1]}
  RG={'Or':[0,2,-3], 'CPos':[0,1,-1]}
  YR={'Or':[-1,2,0], 'CPos':[-1,1,0]}
  YB={'Or':[-1,0,3], 'CPos':[-1,0,1]}
  YO={'Or':[-1,-2,0], 'CPos':[-1,-1,0]}
  YG={'Or':[-1,0,-3], 'CPos':[-1,0,-1]}

  WRB={'Or':[1,2,3], 'CPos':[1,1,1]}
  WOB={'Or':[1,-2,3], 'CPos':[1,-1,1]}
  WOG={'Or':[1,-2,-3], 'CPos':[1,-1,-1]}
  WRG={'Or':[1,2,-3], 'CPos':[1,1,-1]}
  YRB={'Or':[-1,2,3], 'CPos':[-1,1,1]}
  YOB={'Or':[-1,-2,3], 'CPos':[-1,-1,1]}
  YOG={'Or':[-1,-2,-3], 'CPos':[-1,-1,-1]}
  YRG={'Or':[-1,2,-3], 'CPos':[-1,1,-1]}

  corners = {'WRB':WRB, 'WOB':WOB, 'WOG':WOG, 'WRG':WRG, 'YRB':YRB, 'YOB':YOB, 'YOG':YOG, 'YRG':YRG}

  edges={'WR':WR, 'WB':WB, 'WO':WO, 'WG':WG, 'RB':RB, 'OB':OB, 'OG':OG, 'RG':RG, 'YR':YR, 'YB':YB, 'YO':YO, 'YG':YG}

  cube={'C':corners, 'E':edges}

  return cube

def checkPlacement(piece):
  Or=piece['Or']
  Cpos=piece['CPos']
  if Cpos==[Or[0], Or[1]/2, Or[2]/3]:
    return True
  else:
    return False

def whiteCross(cube):
    
    Moves=[]
    pieces=[]
    
    CW=analogMoves['CW']
    ACW=analogMoves['ACW']
    DB=analogMoves['D']
    
    for _ in range(4):
        tempMoves=[]
        for ePiece in cube['E'].values():
            if (not checkPlacement(ePiece)) and (1 in ePiece['Or']):
                CPos,Or=ePiece['CPos'],ePiece['Or']
                
                if 2 in Or:
                    moveRefNum=1
                elif 3 in Or:
                    moveRefNum=0
                elif -3 in Or:
                    moveRefNum=2
                else:
                    moveRefNum=3
                
                if CPos[0]==-1:
                    if Or[0]==1:
                        if CPos[1:3]==[Or[1]/2,Or[2]/3]:
                            tempMoves=[DB[moveRefNum]]
                            break
                        elif CPos[1:3]==[Or[1]/3*-1,Or[2]/2]:
                            tempMoves=['UP',DB[moveRefNum]]
                            break
                        elif CPos[1:3]==[Or[1]/2*-1,Or[2]/3*-1]:
                            tempMoves=['U2',DB[moveRefNum]]
                            break
                        else:
                            tempMoves=['U',DB[moveRefNum]]
                            break
                    else:
                        if (CPos[1]*2+CPos[2]*3)==Or[0]:
                            tempMoves=[CW[moveRefNum],'D',ACW[moveRefNum+1],'DP']
                            break
                        elif (CPos[1]*-3+CPos[2]*2)==Or[0]:
                            tempMoves=[CW[moveRefNum+3],ACW[moveRefNum],ACW[moveRefNum+3]]
                            break
                        elif (CPos[1]*-2+CPos[2]*-3)==Or[0]:
                            tempMoves=['U',ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1]]
                            break
                        else:
                            tempMoves=[ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1]]
                            break
                elif CPos[0]==0:
                    if (CPos[1]==CPos[2] and Or[1]==1) or (CPos[1]!=CPos[2] and Or[2]==1):
                        if (CPos[1]*2==Or[1] or CPos[2]*3==Or[2]):
                            tempMoves=[CW[moveRefNum]]
                            break
                        elif (CPos[1]*3==Or[1] or CPos[2]*-2==Or[2]):
                            tempMoves=['D',CW[moveRefNum+1],'DP']
                            break
                        elif (CPos[1]*-2==Or[1] or CPos[2]*-3==Or[2]):
                            tempMoves=['D2',CW[moveRefNum+2],'D2']
                            break
                        else:
                            tempMoves=['DP',CW[moveRefNum+3],'D']
                    else:
                        if (CPos[1]*2==Or[1] or CPos[2]*3==Or[2]):
                            tempMoves=[ACW[moveRefNum]]
                            break
                        elif (CPos[1]*3==Or[1] or CPos[2]*-2==Or[2]):
                            tempMoves=['D',ACW[moveRefNum+1],'DP']
                            break
                        elif (CPos[1]*-2==Or[1] or CPos[2]*-3==Or[2]):
                            tempMoves=['D2',ACW[moveRefNum+2],'D2']
                            break
                        else:
                            tempMoves=['DP',ACW[moveRefNum+3],'D']
                            break
                else:
                    if Or[0]==1:
                        if CPos[1:3]==[Or[1]/3,-Or[2]/2]:
                            tempMoves=[CW[moveRefNum+1],'D',ACW[moveRefNum+1],'DP']
                            break
                        elif CPos[1:3]==[-Or[1]/2,-Or[2]/3]:
                            tempMoves=[CW[moveRefNum+2],'D2',ACW[moveRefNum+2],'D2']
                            break
                        else:
                            tempMoves=[CW[moveRefNum+3],'DP',ACW[moveRefNum+3],'D']
                            break
                    else:
                        if (CPos[1]*2+CPos[2]*3)==Or[0]:
                            tempMoves=[ACW[moveRefNum],'D',ACW[moveRefNum+1],'DP']
                            break
                        elif (CPos[1]*3+CPos[2]*-2)==Or[0]:
                            tempMoves=[CW[moveRefNum+1],CW[moveRefNum]]
                            break
                        elif (CPos[1]*-3+CPos[2]*2)==Or[0]:
                            tempMoves=[ACW[moveRefNum+3],ACW[moveRefNum]]
                            break
                        else:
                            tempMoves=[CW[moveRefNum+2],'D',CW[moveRefNum+1],'DP']
                    
        s=""
        for token in tempMoves:
            s+=token+' '
        
        if tempMoves!=[]:
            pieces.append(ePiece)
            Moves.append(tempMoves)
        
        cube=shuffleSeq(cube, s)
    
    return cube, Moves, pieces

def whiteFace(cube):
    
    Moves=[]
    
    pieces=[]
    
    CW=analogMoves['CW']
    ACW=analogMoves['ACW']
    DB=analogMoves['D']
    
    for _ in range(4):
        tempMoves=[]
        for cPiece in cube['C'].values():
            if 1 in cPiece['Or'] and not checkPlacement(cPiece):
                Or,CPos=cPiece['Or'],cPiece['CPos']
                
                if sum(Or)==0:
                    moveRefNum=1
                elif sum(Or)==-4:
                    moveRefNum=2
                elif sum(Or)==2:
                    moveRefNum=3
                else:
                    moveRefNum=0
                
                if CPos[0]==1:
                    if Or[0]==1:
                        if (CPos[1]*3+CPos[2]*-2)==(sum(Or)-1):
                            tempMoves=[ACW[1+moveRefNum],'U2',CW[1+moveRefNum],'UP',CW[moveRefNum],ACW[moveRefNum+1],ACW[moveRefNum],CW[moveRefNum+1]]
                            break
                        elif (CPos[1]*-2+CPos[2]*-3)==(sum(Or)-1):
                            tempMoves=[CW[moveRefNum+3],'U2',ACW[moveRefNum+3],ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1],ACW[moveRefNum]]
                            break
                        else:
                            tempMoves=[CW[moveRefNum],"U",ACW[moveRefNum],'U2',ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1],ACW[moveRefNum]]
                    else:
                        if (abs(sum(Or)-1)==5 and abs(Or[0])==2) or (abs(sum(Or)-1)==1 and abs(Or[0])==3):
                            if (CPos[1]*2+CPos[2]*3)==(sum(Or)-1):
                                tempMoves=[ACW[moveRefNum],'UP',CW[moveRefNum],'U',ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1],ACW[moveRefNum]]
                                break
                            elif (CPos[1]*3+CPos[2]*-2)==(sum(Or)-1):
                                tempMoves=[ACW[moveRefNum+1],'U2',DB[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                break
                            elif (CPos[1]*-2+CPos[2]*-3)==(sum(Or)-1):
                                tempMoves=[ACW[moveRefNum+2],"U2",CW[moveRefNum+2],ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1],ACW[moveRefNum]]
                                break
                            else:
                                tempMoves=[ACW[moveRefNum+3],'UP',CW[moveRefNum+3],ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1],ACW[moveRefNum]]
                                break
                        else:
                            if (CPos[1]*2+CPos[2]*3)==(sum(Or)-1):
                                tempMoves=[CW[moveRefNum+1],'U',ACW[moveRefNum+1],'UP',CW[moveRefNum],ACW[moveRefNum+1],ACW[moveRefNum],CW[moveRefNum+1]]
                                break
                            elif (CPos[1]*3+CPos[2]*-2)==(sum(Or)-1):
                                tempMoves=[CW[moveRefNum+2],'U',ACW[moveRefNum+2],CW[moveRefNum],ACW[moveRefNum+1],ACW[moveRefNum],CW[moveRefNum+1]]
                                break
                            elif (CPos[1]*-2+CPos[2]*-3)==(sum(Or)-1):
                                tempMoves=[CW[moveRefNum+3],'U',ACW[moveRefNum+3],ACW[moveRefNum],'U',CW[moveRefNum]]
                                break
                            else:
                                tempMoves=[CW[moveRefNum],'U',DB[moveRefNum],'U2',CW[moveRefNum]]
                                break
                else:
                    if Or[0]==1:
                        if (CPos[1]==CPos[2] and CPos[1:3]==[Or[1]/3,Or[2]/2]) or (CPos[1]!=CPos[2] and CPos[1:3]==[Or[1]/-3,Or[2]/-2]):
                            tempMoves=[CW[moveRefNum+1],'U2',ACW[moveRefNum+1],'UP',CW[moveRefNum],ACW[moveRefNum+1],ACW[moveRefNum],CW[moveRefNum+1]]
                            break
                        elif (CPos[1]!=CPos[2] and CPos[1:3]==[Or[1]/-2,Or[2]/3]) or (CPos[1]==CPos[2] and CPos[1:3]==[Or[1]/2,Or[2]/-3]):
                            tempMoves=['UP',CW[moveRefNum+1],'U2',ACW[moveRefNum+1],'UP',CW[moveRefNum],ACW[moveRefNum+1],ACW[moveRefNum],CW[moveRefNum+1]]
                            break
                        elif (CPos[1]==CPos[2] and CPos[1:3]==[Or[1]/-2,Or[2]/3]) or (CPos[1]!=CPos[2] and CPos[1:3]==[Or[1]/2,Or[2]/-3]):
                            tempMoves=['U',CW[moveRefNum+1],'U2',ACW[moveRefNum+1],'U2',ACW[moveRefNum],'U',CW[moveRefNum]]
                            break
                        else:
                            tempMoves=['U2',CW[moveRefNum+1],'U2',ACW[moveRefNum+1],'UP',CW[moveRefNum],ACW[moveRefNum+1],ACW[moveRefNum],CW[moveRefNum+1]]
                            break
                    else:
                        if (abs(sum(Or)-1)==5 and abs(Or[0])==2) or (abs(sum(Or)-1)==1 and abs(Or[0])==3):
                            if (CPos[1]*2+CPos[2]*3)==(sum(Or)-1):
                                tempMoves=[CW[moveRefNum],ACW[moveRefNum+1],ACW[moveRefNum],CW[moveRefNum+1]]
                                break
                            elif (CPos[1]*-3+CPos[2]*2)==(sum(Or)-1): #left
                                tempMoves=['U',ACW[moveRefNum],'U2',CW[moveRefNum]]
                                break
                            elif (CPos[1]*3+CPos[2]*-2)==(sum(Or)-1): #Right
                                tempMoves=[ACW[moveRefNum],'U',CW[moveRefNum]]
                                break
                            else:
                                tempMoves=[ACW[moveRefNum],'U2',CW[moveRefNum]]
                                break
                        else:
                            if (CPos[1]*2+CPos[2]*3)==(sum(Or)-1):
                                tempMoves=[ACW[moveRefNum+1],CW[moveRefNum],CW[moveRefNum+1],ACW[moveRefNum]]
                                break
                            elif (CPos[1]*-3+CPos[2]*2)==(sum(Or)-1): #left
                                tempMoves=[CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                break
                            elif (CPos[1]*3+CPos[2]*-2)==(sum(Or)-1): #Right
                                tempMoves=['UP',CW[moveRefNum+1],'U2',ACW[moveRefNum+1]]
                                break
                            else:
                                tempMoves=[CW[moveRefNum+1],'U2',ACW[moveRefNum+1]]
                                break
    
        s=""
        for token in tempMoves:
            s+=token+' '
        
        if tempMoves!=[]:
            pieces.append(cPiece)
            Moves.append(tempMoves)
        
        cube=shuffleSeq(cube, s)
    
    return cube, Moves, pieces

def midLayer(cube):
    Moves=[]
    pieces=[]
    
    CW=analogMoves['CW']
    ACW=analogMoves['ACW']
    
    for _ in range(4):
        tempMoves=[]
        for ePiece in cube['E'].values():
            if (-1 not in ePiece['Or']) and (1 not in ePiece['Or']):
                if not checkPlacement(ePiece):
                    CPos, Or=ePiece['CPos'],ePiece['Or']
                    
                    if sum(Or)==-1:
                        moveRefNum=1
                    elif sum(Or)==-5:
                        moveRefNum=2
                    elif sum(Or)==1:
                        moveRefNum=3
                    else:
                        moveRefNum=0
                    
                    if CPos[0]==0:
                        if abs(sum(Or))==1: 
                            if (CPos[1]==CPos[2] and abs(Or[1])==3) or (CPos[1]!=CPos[2] and abs(Or[1])==2): #Correct
                                if CPos[1:3]==[Or[1]/-3,Or[2]/2]: #Assume Left
                                    tempMoves=[CW[moveRefNum],'UP',ACW[moveRefNum],'UP',ACW[moveRefNum+3],'U',CW[moveRefNum+3],'UP',
                                               ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                    break
                                elif CPos[1:3]==[Or[1]/-2,Or[2]/-3]: #opposite
                                    tempMoves=[ACW[moveRefNum+2],'U',CW[moveRefNum+2],'U',CW[moveRefNum+3],'UP',ACW[moveRefNum+3],
                                        'U2',CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                                else: #Assume right
                                    tempMoves=[ACW[moveRefNum+1],'U',CW[moveRefNum+1],'U',CW[moveRefNum+2],'UP',ACW[moveRefNum+2],'U',
                                               CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                            else: #inverted
                                if CPos[1:3]==[Or[1]/-3,Or[2]/-2]:
                                    tempMoves=[ACW[moveRefNum],'U',CW[moveRefNum],'UP',CW[moveRefNum+1],'U2',ACW[moveRefNum+1],'UP',
                                               CW[moveRefNum+1],'U2',ACW[moveRefNum+1]]
                                    break
                                elif CPos[1:3]==[Or[1]/2,Or[2]/-3]:
                                    tempMoves=[CW[moveRefNum],'UP',ACW[moveRefNum],'UP',ACW[moveRefNum+3],'U',CW[moveRefNum+3],'U2',
                                               CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                                elif CPos[1:3]==[Or[1]/-2,Or[2]/3]:
                                    tempMoves=[CW[moveRefNum+2],'UP',ACW[moveRefNum+2],'UP',ACW[moveRefNum+1],'U',CW[moveRefNum+1],
                                               CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                                else:
                                    tempMoves=[ACW[moveRefNum+2],'U',CW[moveRefNum+2],'U',CW[moveRefNum+3],'UP',ACW[moveRefNum+3],'UP',
                                               ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                    break
                        else: #sum 5
                            if (CPos[1]==CPos[2] and abs(Or[1])==2) or (CPos[1]!=CPos[2] and abs(Or[1])==3): #Correct
                                if CPos[1:3]==[Or[1]/-3,Or[2]/2]:
                                    tempMoves=[CW[moveRefNum],'UP',ACW[moveRefNum],'UP',ACW[moveRefNum+3],'U',CW[moveRefNum+3],'UP',
                                               ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                    break
                                elif CPos[1:3]==[Or[1]/-2,Or[2]/-3]:
                                    tempMoves=[ACW[moveRefNum+2],'U',CW[moveRefNum+2],'U',CW[moveRefNum+3],'UP',ACW[moveRefNum+3],'U2',
                                               CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                                else:
                                    tempMoves=[ACW[moveRefNum+1],'U',CW[moveRefNum+1],'U',CW[moveRefNum+2],'UP',ACW[moveRefNum+2],'U',
                                               CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                            else: #inverted
                                if CPos[1:3]==[Or[1]/3,Or[2]/2]:
                                    tempMoves=[CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'U',ACW[moveRefNum],'U2',CW[moveRefNum],'U',
                                               ACW[moveRefNum],'U2',CW[moveRefNum]]
                                    break
                                elif CPos[1:3]==[Or[1]/-2,Or[2]/3]:
                                    tempMoves=[CW[moveRefNum],'UP',ACW[moveRefNum],'UP',ACW[moveRefNum+3],'U',CW[moveRefNum+3],'U2',
                                               CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                                elif CPos[1:3]==[Or[1]/-3,Or[2]/-2]:
                                    tempMoves=[CW[moveRefNum+3],'UP',ACW[moveRefNum+3],'UP',ACW[moveRefNum+2],'U',CW[moveRefNum+2],'U',
                                               CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                    break
                                else:
                                    tempMoves=[ACW[moveRefNum+1],'U',CW[moveRefNum+1],'U',CW[moveRefNum+2],'UP',ACW[moveRefNum+2],'U2',
                                               ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                    break
                    else:
                        if (abs(Or[0])==2 and Or[0]/2==sum(Or[1:3])/3) or (abs(Or[0])==3 and (Or[0]/3==sum(Or[1:3])/-2)):
                            if (CPos[1:3]==[Or[1]/2,Or[2]/3]):
                                tempMoves=['U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                break
                            elif (CPos[1:3]==[Or[1]/-3,Or[2]/2]):
                                tempMoves=[CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                break
                            elif (CPos[1:3]==[Or[1]/-2,Or[2]/-3]):
                                tempMoves=['UP',CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                break
                            else:
                                tempMoves=['U2',CW[moveRefNum+1],'UP',ACW[moveRefNum+1],'UP',ACW[moveRefNum],'U',CW[moveRefNum]]
                                break
                        else:
                            if (CPos[1:3]==[Or[1]/-3,Or[2]/2]):
                                tempMoves=['U2',ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                break
                            elif (CPos[1:3]==[Or[1]/-2,Or[2]/-3]):
                                tempMoves=['U',ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                break
                            elif (CPos[1:3]==[Or[1]/3,Or[2]/-2]):
                                tempMoves=[ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                break
                            else:
                                tempMoves=['UP',ACW[moveRefNum],'U',CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1]]
                                break
        
        s=""
        for token in tempMoves:
            s+=token+' '
        
        if tempMoves!=[]:
            pieces.append({'CPos':CPos,'Or':Or})
            Moves.append(tempMoves)
        
        cube=shuffleSeq(cube, s)
    
    return cube, Moves, pieces

def OLL(cube):
    Moves=[]
    
    CW=analogMoves['CW']
    ACW=analogMoves['ACW']
    
    for _ in range(10):
        tempMoves=[]
        edges,corners=cube['E'],cube['C']
        
        YR,YB,YG,YO=edges['YR'],edges['YB'],edges['YG'],edges['YO']
        YRG,YRB,YOG,YOB=corners['YRG'],corners['YRB'],corners['YOG'],corners['YOB']
        
        yE=[YR['Or'][0],YO['Or'][0],YG['Or'][0],YB['Or'][0]]
        yC=[YRB['Or'][0],YOB['Or'][0],YRG['Or'][0],YOG['Or'][0]]
        
        if yE.count(-1)==0:
            tempMoves=["F",'R','U','RP','UP','FP']
        elif yE.count(-1)==2:
            if yE[0:2].count(-1)==2:
                tempMoves=['L','F','U','FP','UP','LP']
            elif yE[2:4].count(-1)==2:
                tempMoves=['F','R','U','RP','UP','FP']
            else:
                if (YO['Or'][0]==-1 and YB['Or'][0]==-1):
                    moveRefNum=1
                elif (YG['Or'][0]==-1 and YO['Or'][0]==-1):
                    moveRefNum=0
                elif (YB['Or'][0]==-1 and YR['Or'][0]==-1):
                    moveRefNum=2
                else:
                    moveRefNum=3
                tempMoves=[CW[moveRefNum],'U',CW[moveRefNum+1],'UP',ACW[moveRefNum+1],ACW[moveRefNum]]
        else:
            if yC.count(-1)==0:
                tempMoves=['R','U','RP','U','R','U2','RP']
            elif yC.count(-1)==1:
                if YRB['Or'][0]==-1:
                    moveRefNum=1
                elif YRG['Or'][0]==-1:
                    moveRefNum=2
                elif YOG['Or'][0]==-1:
                    moveRefNum=3
                else:
                    moveRefNum=0
                tempMoves=[CW[moveRefNum+1],'U',ACW[moveRefNum+1],'U',CW[moveRefNum+1],'U2',ACW[moveRefNum+1]]
            elif yC.count(-1)==2:
                if (YOB['Or'][0]==-1 and YRB['Or'][0]==-1):
                    moveRefNum=2
                elif (YOG['Or'][0]==-1 and YOB['Or'][0]==-1):
                    moveRefNum=1
                elif (YRB['Or'][0]==-1 and YRG['Or'][0]==-1):
                    moveRefNum=3
                else:
                    moveRefNum=0
                tempMoves=[CW[moveRefNum+1],'U',ACW[moveRefNum+1],'U',CW[moveRefNum+1],'U2',ACW[moveRefNum+1]]
            else:
                break
        Moves.append(tempMoves)
        s=""
        for token in tempMoves:
            s+=token+' '
        
        cube=shuffleSeq(cube, s)
    
    return cube, Moves

def PLL(cube):
    Moves=[]
    
    CW=analogMoves['CW']
    ACW=analogMoves['ACW']
    DB=analogMoves['D']
    
    for i in range(10):
        tempMoves=[]
        edges, corners=cube['E'],cube['C']
        
        YR,YB,YG,YO=edges['YR'],edges['YB'],edges['YG'],edges['YO']
        YRG,YRB,YOG,YOB=corners['YRG'],corners['YRB'],corners['YOG'],corners['YOB']
        
        CRed=[YRB['Or'][1],YRG['Or'][1]]
        COrange=[YOG['Or'][1],YOB['Or'][1]]
        CBlue=[YOB['Or'][2],YRB['Or'][2]]
        CGreen=[YRG['Or'][2],YOG['Or'][2]]
        
        SRed=[YR['Or'][1]]
        SRed.extend(CRed)
        SOrange=[YO['Or'][1]]
        SOrange.extend(COrange)
        SBlue=[YB['Or'][2]]
        SBlue.extend(CBlue)
        SGreen=[YG['Or'][2]]
        SGreen.extend(CGreen)
        
        CSum=[-6,-4,4,6]
        SSum=[-9,-6,6,9]
        
        if sum(SRed)==6 and sum(SGreen)==-9 and sum(SBlue)==9 and sum(SOrange)==-6:
            break
        else:
            if sum(SRed) in SSum and sum(SGreen) in SSum and sum(SBlue) in SSum and sum(SOrange) in SSum:
                if sum(SRed)==-9:
                    tempMoves=['UP']
                elif sum(SRed)==-6:
                    tempMoves=['U2']
                else:
                    tempMoves=['U']
            else:
                if sum(CRed) in CSum and sum(CGreen) in CSum and sum(CBlue) in CSum and sum(COrange) in CSum:
                    if sum(SRed) in SSum or sum(SGreen) in SSum or sum(SBlue) in SSum or sum(SOrange) in SSum:
                        if sum(SRed) in SSum:
                            moveRefNum=3
                            if SOrange[0]==CGreen[0]:
                                tempMoves=[DB[moveRefNum],'U',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'U',DB[moveRefNum]]
                            else:
                                tempMoves=[DB[moveRefNum],'UP',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'UP',DB[moveRefNum]]
                        elif sum(SGreen) in SSum:
                            moveRefNum=0
                            if SBlue[0]==COrange[0]:
                                tempMoves=[DB[moveRefNum],'U',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'U',DB[moveRefNum]]
                            else:
                                tempMoves=[DB[moveRefNum],'UP',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'UP',DB[moveRefNum]]
                        elif sum(SBlue) in SSum:
                            moveRefNum=2
                            if SGreen[0]==CRed[0]:
                                tempMoves=[DB[moveRefNum],'U',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'U',DB[moveRefNum]]
                            else:
                                tempMoves=[DB[moveRefNum],'UP',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'UP',DB[moveRefNum]]
                        else:
                            moveRefNum=1
                            if SOrange[0]==CGreen[0]:
                                tempMoves=[DB[moveRefNum],'U',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'U',DB[moveRefNum]]
                            else:
                                tempMoves=[DB[moveRefNum],'UP',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                           ACW[moveRefNum+3],CW[moveRefNum+1],'UP',DB[moveRefNum]]
                    else:
                        moveRefNum=1
                        tempMoves=[DB[moveRefNum],'U',ACW[moveRefNum+1],CW[moveRefNum+3],DB[moveRefNum],
                                   ACW[moveRefNum+3],CW[moveRefNum+1],'U',DB[moveRefNum]]
                else:
                    if sum(CRed) in CSum:
                        moveRefNum=3
                        tempMoves=[ACW[moveRefNum+1],CW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],
                                   CW[moveRefNum+1],ACW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],DB[moveRefNum+1]]
                    elif sum(CBlue) in CSum:
                        moveRefNum=2
                        tempMoves=[ACW[moveRefNum+1],CW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],
                                   CW[moveRefNum+1],ACW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],DB[moveRefNum+1]]
                    elif sum(CGreen) in CSum:
                        moveRefNum=0
                        tempMoves=[ACW[moveRefNum+1],CW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],
                                   CW[moveRefNum+1],ACW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],DB[moveRefNum+1]]
                    else:
                        moveRefNum=1
                        tempMoves=[ACW[moveRefNum+1],CW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],
                                   CW[moveRefNum+1],ACW[moveRefNum],ACW[moveRefNum+1],DB[moveRefNum+2],DB[moveRefNum+1]]
        if tempMoves!=[]:
            Moves.append(tempMoves)
            s=""
            for token in tempMoves:
                s+=token+' '
            
            cube=shuffleSeq(cube, s)
    
    return cube, Moves

def solve(cube):
    
    print("\nWhite Cross:")
    cube,Moves,Pieces=whiteCross(cube)
    for i in range(len(Moves)):
        print("Piece: ", Pieces[i])
        print(Moves[i])
    
    print("\nWhite Face:")
    cube,Moves,Pieces=whiteFace(cube)
    for i in range(len(Moves)):
        print("Piece: ", Pieces[i])
        print(Moves[i])
    
    print("\nMiddle Layer:")
    cube,Moves,Pieces=midLayer(cube)
    for i in range(len(Moves)):
        print("Piece: ", Pieces[i])
        print(Moves[i])
    
    print("\nOLL:")
    cube,Moves=OLL(cube)
    for i in range(len(Moves)):
        print(Moves[i])
        
    print("\nPLL:")
    cube,Moves=PLL(cube)
    for i in range(len(Moves)):
        print(Moves[i])

def shadowSolve(cube):
        
    cube,Moves,Pieces=whiteCross(cube)
    
    cube,Moves,Pieces=whiteFace(cube)
    
    cube,Moves,Pieces=midLayer(cube)
    
    cube,Moves=OLL(cube)
    
    cube,Moves=PLL(cube)
    
    return cube


def testAlg(cube):
    solvedCube=reset()
    for _ in range(10000):
        print(_)
        cube,shuffMoves=shuffleRandom(cube)
        cube=shadowSolve(cube)
        if cube!=solvedCube:
            print("Number of Iterations:",_)
            print(shuffMoves)
            cube=reset()
            s=''
            for token in shuffMoves:
                s+=token+' '
            cube=shuffleSeq(cube,s)
            solve(cube)
            break
        

def inputCube():
    print("\n Enter your configuration, separate rows by enter, separate row elements by space:")
    WR1=input("\nEnter the first white row, red facing up: ")
    WR1=WR1.split()
    WR2=input("Enter the second white row, red facing up: ")
    WR2=WR2.split()
    WR3=input("Enter the third white row, red facing up: ")
    WR3=WR3.split()
    
    RR1=input("\nEnter the first red row, yellow facing up: ")
    RR1=RR1.split()
    RR2=input("Enter the second red row, yellow facing up: ")
    RR2=RR2.split()
    RR3=input("Enter the third red row, yellow facing up: ")
    RR3=RR3.split()
    
    GR1=input("\nEnter the first green row, yellow facing up: ")
    GR1=GR1.split()
    GR2=input("Enter the second green row, yellow facing up: ")
    GR2=GR2.split()
    GR3=input("Enter the third green row, yellow facing up: ")
    GR3=GR3.split()
    
    OR1=input("\nEnter the first orange row, yellow facing up: ")
    OR1=OR1.split()
    OR2=input("Enter the second orange row, yellow facing up: ")
    OR2=OR2.split()
    OR3=input("Enter the third orange row, yellow facing up: ")
    OR3=OR3.split()
    
    BR1=input("\nEnter the first blue row, yellow facing up: ")
    BR1=BR1.split()
    BR2=input("Enter the second blue row, yellow facing up: ")
    BR2=BR2.split()
    BR3=input("Enter the third blue row, yellow facing up: ")
    BR3=BR3.split()
    
    YR1=input("\nEnter the first yellow row, red facing up: ")
    YR1=YR1.split()
    YR2=input("Enter the second yellow row, red facing up: ")
    YR2=YR2.split()
    YR3=input("Enter the third yellow row, red facing up: ")
    YR3=YR3.split()
    
    WR={'Or':[int(WR1[1]),int(RR3[1]),0], 'CPos':[1,1,0]}
    WB={'Or':[int(WR2[0]),0,int(BR3[1])], 'CPos':[1,0,1]}
    WO={'Or':[int(WR3[1]),int(OR3[1]),0], 'CPos':[1,-1,0]}
    WG={'Or':[int(WR2[2]),0,int(GR3[1])], 'CPos':[1,0,-1]}
    RB={'Or':[0,int(RR2[0]),int(BR2[2])], 'CPos':[0,1,1]}
    OB={'Or':[0,int(OR2[2]),int(BR2[0])], 'CPos':[0,-1,1]}
    OG={'Or':[0,int(OR2[0]),int(GR2[2])], 'CPos':[0,-1,-1]}
    RG={'Or':[0,int(RR2[2]),int(GR2[0])], 'CPos':[0,1,-1]}
    YR={'Or':[int(YR1[1]),int(RR1[1]),0], 'CPos':[-1,1,0]}
    YB={'Or':[int(YR2[0]),0,int(BR1[1])], 'CPos':[-1,0,1]}
    YO={'Or':[int(YR3[1]),int(OR1[1]),0], 'CPos':[-1,-1,0]}
    YG={'Or':[int(YR2[2]),0,int(GR1[1])], 'CPos':[-1,0,-1]}

    WRB={'Or':[int(WR1[0]),int(RR3[0]),int(BR3[2])], 'CPos':[1,1,1]}
    WOB={'Or':[int(WR3[0]),int(OR3[2]),int(BR3[0])], 'CPos':[1,-1,1]}
    WOG={'Or':[int(WR3[2]),int(OR3[0]),int(GR3[2])], 'CPos':[1,-1,-1]}
    WRG={'Or':[int(WR1[2]),int(RR3[2]),int(GR3[0])], 'CPos':[1,1,-1]}
    YRB={'Or':[int(YR1[0]),int(RR1[0]),int(BR1[2])], 'CPos':[-1,1,1]}
    YOB={'Or':[int(YR3[0]),int(OR1[2]),int(BR1[0])], 'CPos':[-1,-1,1]}
    YOG={'Or':[int(YR3[2]),int(OR1[0]),int(GR1[2])], 'CPos':[-1,-1,-1]}
    YRG={'Or':[int(YR3[2]),int(RR1[2]),int(GR1[0])], 'CPos':[-1,1,-1]}

    corners = {'WRB':WRB, 'WOB':WOB, 'WOG':WOG, 'WRG':WRG, 'YRB':YRB, 'YOB':YOB, 'YOG':YOG, 'YRG':YRG}

    edges={'WR':WR, 'WB':WB, 'WO':WO, 'WG':WG, 'RB':RB, 'OB':OB, 'OG':OG, 'RG':RG, 'YR':YR, 'YB':YB, 'YO':YO, 'YG':YG}

    cube={'C':corners, 'E':edges}
    
    return cube

#Defining Essential Variables

dict_num={1:U, 2:UP, 4:D, 5:DP, 7:R, 8:RP, 10:L, 11:LP, 13:F, 14:FP, 16:B, 17:BP, 3:U2, 6:D2, 9:R2, 12:L2, 15:F2, 18:B2}

dict_alpha={'U':U, 'UP':UP, 'D':D, 'DP':DP, 'R':R, 'RP':RP, 'L':L, 'LP':LP, 'F':F,'FP':FP, 'B':B, 'BP':BP, 'U2':U2, 'D2':D2, 'R2':R2, 'L2':L2, 'F2':F2, 'B2':B2}
dict_num_alpha={1:'U', 2:'UP', 4:'D', 5:'DP', 7:'R', 8:'RP', 10:'L', 11:'LP', 13:'F',14:'FP', 16:'B', 17:'BP', 3:'U2', 6:'D2', 9:'R2', 12:'L2', 15:'F2', 18:'B2'}
dict_alpha_num={'U':1, 'UP':2, 'D':4, 'DP':5, 'R':7, 'RP':8, 'L':10, 'LP':11, 'F':13, 'FP':14, 'B':16, 'BP':17, 'U2':3, 'D2':6, 'R2':9, 'L2':12, 'F2':15, 'B2':18}

groups=(('F','FP','F2','B','B2','BP'),('R','RP','R2','L','L2','LP'),('U','U2','UP','D','DP','D2'))

analogMoves={'CW':('L','F','R','B','L','F','R'), 'ACW':('LP','FP','RP','BP','LP','FP','RP'), 'D':('L2','F2','R2','B2','L2','F2','R2')}

#

while True:
    
    print("\n",'*'*25)
    print("\t"*4, "Menu")
    print("\t1. Input Cube")
    print("\t2. Display Cube")
    print("\t3. Shuffle Randomly")
    print("\t4. Shuffle Sequentially")
    print("\t5. Reset Cube")
    print("\t6. Solve Cube")
    print("\t7.", "Quit")
    
    ch=input("\n \t Enter your choice:")
    
    if ch.isdigit():
        if int(ch)==1:
            cube=inputCube()
            print("\nCube Entered!")
        elif int(ch)==2:
            displayCube(cube)
        elif int(ch)==3:
            cube,shuffMoves=shuffleRandom(cube)
            print("Shuffle Moves:", shuffMoves)
        elif int(ch)==4:
            s=input("Enter your Moves separated by a space:")
            cube=shuffleSeq(s)
            print("\n\tShuffled!")
        elif int(ch)==5:
            cube=reset()
            print("\n\\t Cube Reset!")
        elif int(ch)==6:
            solve(cube)
            print("\nCube Solved!")
        elif int(ch)==7:
            print("\n\t Program Terminated!")
            break
        else:
            print("\nInvalid Input")
    else:
        print("\nInvalid Input")
