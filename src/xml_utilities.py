from xml.etree import ElementTree
import datetime
import numpy
import pandas

DEFAULT_NAMESPACE = NS = "{http://www.tei-c.org/ns/1.0}"

def makeBorrowingDataFrame(fileName):
    document = parseXMLDocument(fileName)
    borrowingEventNodes = getAllBorrowingEventNodes(document)
    borrowedEventData = [getBorrowingEventData(
        node) for node in borrowingEventNodes]
    return pandas.DataFrame(borrowedEventData)


def parseXMLDocument(filename):
    return ElementTree.parse(filename)


def getAllBorrowingEventNodes(document):
    return document.findall(f".//{NS}ab[{NS}bibl]")


def getBorrowingEventData(borrowingEvent):
    return {"Title": getTitle(borrowingEvent),
            "DateBorrowed": getDateBorrowed(borrowingEvent),
            "DateReturned": getDateReturned(borrowingEvent)
            }


def getTitle(borrowingEvent):
    titleNode = getTitleNode(borrowingEvent)
    if titleNode is None:
        return str()
    else:
        return titleNode.text


def getTitleNode(borrowingEvent):
    return borrowingEvent.find(f".{NS}bibl[@ana='#borrowedItem']/{NS}title")


def getDateBorrowed(borrowingEvent):
    dateBorrowedNode = getDateBorrowedNode(borrowingEvent)
    return parseDateNodeIntoDate(dateBorrowedNode)


def getDateBorrowedNode(borrowingEvent):
    return borrowingEvent.find(f".{NS}date[@ana='#checkedOut']")


def getDateReturned(borrowingEvent):
    dateReturnedNode = getDataReturnedNode(borrowingEvent)
    return parseDateNodeIntoDate(dateReturnedNode)


def getDataReturnedNode(borrowingEvent):
    return borrowingEvent.find(f".{NS}date[@ana='#returned']")


def parseDateNodeIntoDate(dateNode):
    if dateNode is None:
        return numpy.datetime64("NaT")
    else:
        date = dateNode.get("when")
        if date is None:
            return numpy.datetime64("NaT")
        else:
            return stringToDate(date)


def stringToDate(dateString):
    try:
        return datetime.datetime.strptime(dateString, "%Y-%m-%d").date()
    except ValueError:
        try:
            return datetime.datetime.strptime(dateString, "%Y-%m").date()
        except ValueError:
            try:
                return datetime.datetime.strptime(dateString, "%Y").date()
            except ValueError:
                return numpy.datetime64("NaT")
