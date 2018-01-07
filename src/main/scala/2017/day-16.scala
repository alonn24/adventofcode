package adventofcode2017

import scala.io.Source

object Day16 {
  lazy val moves: String = Source.fromFile(s"2017/input/day-16.input").mkString.trim
  val input = "abcdefghijklmnop".toArray
  
  val actions: Map[Char, (Array[Char], String, String) => Array[Char]] = Map[Char, (Array[Char], String, String) => Array[Char]] (
    's' -> { case (input, x, _) => 
      val cutPoint = input.length - x.toInt;
      input.slice(cutPoint, input.length) ++ input.slice(0, cutPoint)
    },
    'x' -> { case (input, a, b) => 
      val temp = input(a.toInt);
      input(a.toInt) = input(b.toInt)
      input(b.toInt) = temp;
      input
    },
    'p' -> { case (num, a, b) => 
      actions('x')(num, num.indexOf(a(0)).toString, num.indexOf(b(0)).toString);
    }
  )

  def performMove(input: Array[Char], move:String): Array[Char] = {
    val action = move(0);
    val params = move.substring(1).split("/").toArray;
    val f = actions(action)
    f(input, params(0), if (params.length == 2) params(1) else "");
  }

  def findLoopIndex(input: Array[Char], movesOrder: Array[String], cache: Set[String] = Set(input.mkString), times: Int = 0): Int = {
    val newInput = movesOrder.foldLeft(input) {
      (input, move) => performMove(input, move)
    }
    if (cache(newInput.mkString)) times + 1 
    else findLoopIndex(newInput, movesOrder, cache + newInput.mkString, times + 1)
  }

  def main(args: Array[String]): Unit = {
    val movesOrder = moves.split(",");

    val oneDance = movesOrder.foldLeft(input) {
      (input, move) => performMove(input, move)
    }
    println(s"part1: ${oneDance.mkString}")

    val loopIndex = findLoopIndex(input, movesOrder)
    val start = Math.floor(1000000000/loopIndex)*loopIndex;
    val res = (start.toInt until 1000000000).foldLeft(input) {
      (input, _) => movesOrder.foldLeft(input) {
        (input, move) => performMove(input, move)
      }
    }
    println(s"part2: ${res.mkString}")
  }
}
