#!/bin/bash

PRINTER_NAME="Brother_HL-2060"

FILE=$1

lpr -P "${PRINTER_NAME}" -o number-up=2 -o prettyprint "${FILE}"

