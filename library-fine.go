package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'libraryFine' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER d1
 *  2. INTEGER m1
 *  3. INTEGER y1
 *  4. INTEGER d2
 *  5. INTEGER m2
 *  6. INTEGER y2
 */

func libraryFine(d1 int32, m1 int32, y1 int32, d2 int32, m2 int32, y2 int32) int32 {
    // Write your code here
    var fine int32 = 0

    if d1 <= d2 && m1 <= m2 && y1 <= y2 {
        return fine
    }
    if y1 > y2{
        fine = 10000
    } else if y1 == y2 && m1 > m2 {
        fine = 500 * (m1 - m2)
    } else if y1 == y2 && m1 == m2 && d1 > d2 {
        fine = 15 * (d1 - d2)
    }
        
    return fine
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    d1Temp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
    checkError(err)
    d1 := int32(d1Temp)

    m1Temp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
    checkError(err)
    m1 := int32(m1Temp)

    y1Temp, err := strconv.ParseInt(firstMultipleInput[2], 10, 64)
    checkError(err)
    y1 := int32(y1Temp)

    secondMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    d2Temp, err := strconv.ParseInt(secondMultipleInput[0], 10, 64)
    checkError(err)
    d2 := int32(d2Temp)

    m2Temp, err := strconv.ParseInt(secondMultipleInput[1], 10, 64)
    checkError(err)
    m2 := int32(m2Temp)

    y2Temp, err := strconv.ParseInt(secondMultipleInput[2], 10, 64)
    checkError(err)
    y2 := int32(y2Temp)

    result := libraryFine(d1, m1, y1, d2, m2, y2)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
