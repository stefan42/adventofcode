module Lib
    ( solution1
    , solution2
    ) where

import qualified Data.Set as SET

type Coord = (Int, Int)

calcNextCoord :: Coord -> Char -> Coord
calcNextCoord (x,y) c
  = case c of
      '>' -> (x+1,y)
      '<' -> (x-1,y)
      'v' -> (x,y+1)
      '^' -> (x,y-1)
      _   -> (x,y)

input2Coords :: String -> [Coord] -> [Coord]
input2Coords [] rs = rs
input2Coords (c:cs) (r:rs) = input2Coords cs (newCoord:r:rs)
  where
  newCoord = calcNextCoord r c

processContent1 :: String -> Int
processContent1 content = SET.size $ SET.fromList $ input2Coords content [(0,0)]

splitInput :: String -> (String, String)
splitInput xs = splitInput' xs ("","")
  where
  splitInput' :: String -> (String, String) -> (String, String)
  splitInput' [] (s1,s2) = (s1,s2)
  splitInput' (c1:[]) (s1,s2) = (s1 ++ [c1], s2)
  splitInput' (c1:c2:cs) (s1,s2) = splitInput' cs (s1 ++ [c1], s2 ++ [c2])

processContent2 :: String -> Int
processContent2 content = SET.size $ SET.union s1 s2
  where
  s1 = SET.fromList $ input2Coords content1 [(0,0)]
  s2 = SET.fromList $ input2Coords content2 [(0,0)]
  (content1, content2) = splitInput content

solution1 :: IO ()
solution1
  = do
    content <- readFile "input.txt"
    putStrLn $ "result " ++ show (processContent1 content)

solution2 :: IO ()
solution2
  = do
    content <- readFile "input.txt"
    putStrLn $ "result " ++ show (processContent2 content)
