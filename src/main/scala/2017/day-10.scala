package adventofcode2017

object Day10 {
  lazy val input: String = "227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144"

  def sparseHash(nums: List[Int], times: Int, listLength: Int): List[Int] = {
    val list = (0 until listLength).toList ++ (0 until listLength).toList
    val (res, _, _) = (0 until times).foldLeft((list, 0, 0)) {
      case ((list, pos, skip), _) => 
        val (newList, newPos, newSkip) = nums.foldLeft((list, pos, skip)) {
          case ((list, pos, skip), n) => 
            val part = list.slice(pos, pos + n).reverse
            val loopI = part.length - Math.max(pos + n - listLength, 0);
            val partToStart = part.slice(loopI, part.length);
            val half = partToStart ++
              list.slice(partToStart.length, pos) ++
              part.slice(0, loopI) ++
              list.slice(pos+n, list.length)
              val nextList = half.slice(0, listLength) ++ half.slice(0, listLength)
            (nextList, (pos + n + skip) % listLength, skip+1)
        }
        (newList, newPos, newSkip)
      
    }
    res.slice(0, listLength)
  }

  def denseHash(nums: List[Int]): List[Int] = {
    val res = (0 until 16).foldLeft(List[Int]()) { (x, i) => 
      val value = nums.slice(i*16, i*16+16).foldLeft(0)(_^_)
      x :+ value
    }
    res
  }

  def main(args: Array[String]): Unit = {
    val nums = input.toCharArray.map(_.toInt).toList ++ List(17, 31, 73, 47, 23)
    val sparseHashVal = sparseHash(nums, 64, 256)
    val denseHashVal = denseHash(sparseHashVal);
    val knotHash = denseHashVal.foldLeft("") { (res, n) => 
      res + (s"0${n.toHexString}" takeRight 2)
    }
    println(knotHash)
  }
}