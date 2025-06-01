[5:28 p. m., 1/6/2025] Amor: Sub EvaluarOfertas()
    Dim ultimaFila As Long
    Dim i As Long
    Dim menorValor As Double
    Dim celda As Range

    ' Determinar la última fila con datos en la columna A
    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    ' Borrar columnas B, C y D por si hay datos antiguos
    Range("B2:D" & ultimaFila).ClearContents

    ' Calcular valores redondeados en columna B y visualización
    For i = 2 To ultimaFila
        Cells(i, 2).Value = Round(Cells(i, 1).Value, 4) ' Columna B: Redondeado a 4 decimales
    Next i

    ' Encontrar el menor valor real (sin redondear)
    menorValor = Cells(2, 1).Value
    For i = 3 To ultimaFila
        If Cells(i, 1).Value < menorValor Then
            menorValor = Cells(i, 1).Value
        End If
    Next i

    '…
[5:50 p. m., 1/6/2025] Amor: Sub EvaluarOfertas()
    Dim ultimaFila As Long
    Dim i As Long
    Dim menorValor As Double

    ' Determina la última fila con datos en la columna A
    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    ' Limpia columnas B y C
    Range("B2:C" & ultimaFila).ClearContents

    ' Redondea a 4 decimales (simulación visual)
    For i = 2 To ultimaFila
        Cells(i, 2).Value = Round(Cells(i, 1).Value, 4)
    Next i

    ' Encuentra el menor valor real
    menorValor = Cells(2, 1).Value
    For i = 3 To ultimaFila
        If Cells(i, 1).Value < menorValor Then
            menorValor = Cells(i, 1).Value
        End If
    Next i

    ' Marca al ganador y aplica formato
    For i = 2 To ultimaFila
        If Cells(i, 1).Value = menorValor Then
            Cells(i, 3).Value = "MENOR"
            Cells(i, 1).Interior.Color = RGB(198, 239, 206) ' Verde claro
            Cells(i, 2).Interior.Color = RGB(198, 239, 206)
            Cells(i, 3).Interior.Color = RGB(198, 239, 206)
        End If
    Next i

    ' Encabezados
    Range("A1").Value = "Valor Real"
    Range("B1").Value = "Visual (4 decimales)"
    Range("C1").Value = "¿Ganador?"

    MsgBox "Evaluación completada. El menor valor real ha sido identificado.", vbInformation
End Sub
