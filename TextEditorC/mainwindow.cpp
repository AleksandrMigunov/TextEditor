/* Copyright (C) 2022 Aleksandr Migunov

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
  
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>. */


#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtCore>
#include <QtGui>
#include <QWidget>
#include <QMainWindow>
#include <QMessageBox>
#include <QInputDialog>
#include <QFileDialog>
#include <QFontDialog>
#include <QColorDialog>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

//closing the program
void MainWindow::closeEvent(QCloseEvent *event) {
    QMessageBox* messagebox = new QMessageBox (QMessageBox::Question,
                                               tr("Confirm Dialog"), tr("Really quit?"),
                                               QMessageBox::Yes | QMessageBox::No, this);
    messagebox->setButtonText(QMessageBox::Yes, tr("Yes"));
    messagebox->setButtonText(QMessageBox::No, tr("No"));
    int n = messagebox->exec();
    delete messagebox;

    if (n == QMessageBox::Yes) {
        event->accept();
    } else {
        event->ignore();
    }
}

void MainWindow::on_actionExit_triggered()
{
    close();
}

void MainWindow::on_actionNew_Text_1_triggered()
{
    int answer = QMessageBox::question(this, "Clear Text", "Do you want to clear the text?", QMessageBox::No | QMessageBox::Yes);
    if (answer == QMessageBox::Yes) {
        ui->textEdit_Text_1->clear();
    }
}

void MainWindow::on_actionNew_Text_2_triggered()
{
    int answer = QMessageBox::question(this, "Clear Text", "Do you want to clear the text?", QMessageBox::No | QMessageBox::Yes);
    if (answer == QMessageBox::Yes) {
        ui->textEdit_Text_2->clear();
    }
}

void MainWindow::on_actionNew_Text_3_triggered()
{
    int answer = QMessageBox::question(this, "Clear Text", "Do you want to clear the text?", QMessageBox::No | QMessageBox::Yes);
    if (answer == QMessageBox::Yes) {
        ui->textEdit_Text_3->clear();
    }
}

void MainWindow::on_actionOpen_Text_1_triggered()
{
    QString file = QFileDialog::getOpenFileName(this, "Open file", "",
                                              "HTML Files (*.html);;Text Files (*.txt);;Paratext Files (*.SFM *.sfm)");
    if (!file.isEmpty())
    {
        QFile File(file);
        if(File.open(QFile::ReadOnly | QFile::Text))
        {
            QTextStream in(&File);
            in.setCodec("UTF-8");

            QString text = in.readAll();
            File.close();
            //ui->textEdit_Text_1->setAcceptRichText(false);
            ui->textEdit_Text_1->setText(text);

        }
        else {
            QMessageBox::information(this, "Error", "Unable to open file.", QMessageBox::Ok);
        }
    }
}

void MainWindow::on_actionOpen_Text_2_triggered()
{
    QString file = QFileDialog::getOpenFileName(this, "Open file", "",
                                              "HTML Files (*.html);;Text Files (*.txt);;Paratext Files (*.SFM *.sfm)");
    if (!file.isEmpty())
    {
        QFile File(file);
        if(File.open(QFile::ReadOnly | QFile::Text))
        {
            QTextStream in(&File);
            in.setCodec("UTF-8");

            QString text = in.readAll();
            File.close();
            //ui->textEdit_Text_2->setAcceptRichText(false);
            ui->textEdit_Text_2->setText(text);

        }
        else {
            QMessageBox::information(this, "Error", "Unable to open file.", QMessageBox::Ok);
        }
    }
}

void MainWindow::on_actionOpen_Text_3_triggered()
{
    QString file = QFileDialog::getOpenFileName(this, "Open file", "",
                                              "HTML Files (*.html);;Text Files (*.txt);;Paratext Files (*.SFM *.sfm)");
    if (!file.isEmpty())
    {
        QFile File(file);
        if(File.open(QFile::ReadOnly | QFile::Text))
        {
            QTextStream in(&File);
            in.setCodec("UTF-8");

            QString text = in.readAll();
            File.close();
            //ui->textEdit_Text_3->setAcceptRichText(false);
            ui->textEdit_Text_3->setText(text);

        }
        else {
            QMessageBox::information(this, "Error", "Unable to open file.", QMessageBox::Ok);
        }
    }
}

void MainWindow::on_actionSave_Text_1_triggered()
{
    QString file = QFileDialog::getSaveFileName(this, "Save File", "",
                                                "HTML Files (*.html);;Text Files (*.txt);;Paratext Files (*.SFM *.sfm)");
    QFile File(file);
    if(File.open(QFile::WriteOnly | QFile::Text))
    {
        QTextStream out(&File);

        out.setCodec("UTF-8");

        if (file.endsWith(".txt") || file.endsWith(".SFM") || file.endsWith(".sfm")) {
            out << ui->textEdit_Text_1->toPlainText();
        }
        else if (file.endsWith(".htm") || file.endsWith(".html")) {
            out << ui->textEdit_Text_1->toHtml();
        }

        File.flush();
        File.close();
    }
    else {
        QMessageBox::information(this, "Error",
                                 "Unable to save file.", QMessageBox::Ok);
    }
}

void MainWindow::on_actionSave_Text_2_triggered()
{
    QString file = QFileDialog::getSaveFileName(this, "Save File", "",
                                                "HTML Files (*.html);;Text Files (*.txt);;Paratext Files (*.SFM *.sfm)");
    QFile File(file);
    if(File.open(QFile::WriteOnly | QFile::Text))
    {
        QTextStream out(&File);

        out.setCodec("UTF-8");

        if (file.endsWith(".txt") || file.endsWith(".SFM") || file.endsWith(".sfm")) {
            out << ui->textEdit_Text_2->toPlainText();
        }
        else if (file.endsWith(".htm") || file.endsWith(".html")) {
            out << ui->textEdit_Text_2->toHtml();
        }

        File.flush();
        File.close();
    }
    else {
        QMessageBox::information(this, "Error",
                                 "Unable to save file.", QMessageBox::Ok);
    }
}

void MainWindow::on_actionSave_Text_3_triggered()
{
    QString file = QFileDialog::getSaveFileName(this, "Save File", "",
                                                "HTML Files (*.html);;Text Files (*.txt);;Paratext Files (*.SFM *.sfm)");
    QFile File(file);
    if(File.open(QFile::WriteOnly | QFile::Text))
    {
        QTextStream out(&File);

        out.setCodec("UTF-8");

        if (file.endsWith(".txt") || file.endsWith(".SFM") || file.endsWith(".sfm")) {
            out << ui->textEdit_Text_3->toPlainText();
        }
        else if (file.endsWith(".htm") || file.endsWith(".html")) {
            out << ui->textEdit_Text_3->toHtml();
        }

        File.flush();
        File.close();
    }
    else {
        QMessageBox::information(this, "Error",
                                 "Unable to save file.", QMessageBox::Ok);
    }
}


void MainWindow::on_actionUndo_in_Text_1_triggered()
{
    ui->textEdit_Text_1->undo();
}

void MainWindow::on_actionUndo_in_Text_2_triggered()
{
    ui->textEdit_Text_2->undo();
}

void MainWindow::on_actionUndo_in_Text_3_triggered()
{
    ui->textEdit_Text_3->undo();
}

void MainWindow::on_actionRedo_in_Text_1_triggered()
{
    ui->textEdit_Text_1->redo();
}

void MainWindow::on_actionRedo_in_Text_2_triggered()
{
    ui->textEdit_Text_2->redo();
}

void MainWindow::on_actionRedo_in_Text_3_triggered()
{
    ui->textEdit_Text_3->redo();
}

void MainWindow::on_actionCut_from_Text_1_triggered()
{
    ui->textEdit_Text_1->cut();
}

void MainWindow::on_actionCut_from_Text_2_triggered()
{
    ui->textEdit_Text_2->cut();
}

void MainWindow::on_actionCut_from_Text_3_triggered()
{
    ui->textEdit_Text_3->cut();
}

void MainWindow::on_actionCopy_from_Text_1_triggered()
{
    ui->textEdit_Text_1->copy();
}

void MainWindow::on_actionCopy_from_Text_2_triggered()
{
    ui->textEdit_Text_2->copy();
}

void MainWindow::on_actionCopy_from_Text_3_triggered()
{
    ui->textEdit_Text_3->copy();
}

void MainWindow::on_actionPaste_into_Text_1_triggered()
{
    ui->textEdit_Text_1->paste();
}

void MainWindow::on_actionPaste_into_Text_2_triggered()
{
    ui->textEdit_Text_2->paste();
}

void MainWindow::on_actionPaste_into_Text_3_triggered()
{
    ui->textEdit_Text_3->paste();
}

void MainWindow::on_actionSelect_All_in_Text_1_triggered()
{
    ui->textEdit_Text_1->selectAll();
}

void MainWindow::on_actionSelect_All_in_Text_2_triggered()
{
    ui->textEdit_Text_2->selectAll();
}

void MainWindow::on_actionSelect_All_in_Text_3_triggered()
{
    ui->textEdit_Text_3->selectAll();
}


void MainWindow::on_actionZoom_In_Text_1_triggered()
{
    ui->textEdit_Text_1->zoomIn();
}

void MainWindow::on_actionZoom_In_Text_2_triggered()
{
    ui->textEdit_Text_2->zoomIn();
}

void MainWindow::on_actionZoom_In_Text_3_triggered()
{
    ui->textEdit_Text_3->zoomIn();
}

void MainWindow::on_actionZoom_Out_Text_1_triggered()
{
    ui->textEdit_Text_1->zoomOut();
}

void MainWindow::on_actionZoom_Out_Text_2_triggered()
{
    ui->textEdit_Text_2->zoomOut();
}

void MainWindow::on_actionZoom_Out_Text_3_triggered()
{
    ui->textEdit_Text_3->zoomOut();
}

void MainWindow::on_actionFind_in_Text_1_triggered()
{
    QString find_text = QInputDialog::getText(this, "SearchText", "Find: ");
    if (ui->textEdit_Text_1->isReadOnly() == false) {
        ui->textEdit_Text_1->moveCursor(QTextCursor::Start);
        QColor color = QColor(Qt::yellow);
        while (ui->textEdit_Text_1->find(find_text)) {
            ui->textEdit_Text_1->setTextBackgroundColor(color);
            ui->textEdit_Text_1->textCursor();
        }
    }
}

void MainWindow::on_actionFind_in_Text_2_triggered()
{
    QString find_text = QInputDialog::getText(this, "SearchText", "Find: ");
    if (ui->textEdit_Text_2->isReadOnly() == false) {
        ui->textEdit_Text_2->moveCursor(QTextCursor::Start);
        QColor color = QColor(Qt::yellow);
        while (ui->textEdit_Text_2->find(find_text)) {
            ui->textEdit_Text_2->setTextBackgroundColor(color);
            ui->textEdit_Text_2->textCursor();
        }
    }
}

void MainWindow::on_actionFind_in_Text_3_triggered()
{
    QString find_text = QInputDialog::getText(this, "SearchText", "Find: ");
    if (ui->textEdit_Text_3->isReadOnly() == false) {
        ui->textEdit_Text_3->moveCursor(QTextCursor::Start);
        QColor color = QColor(Qt::yellow);
        while (ui->textEdit_Text_3->find(find_text)) {
            ui->textEdit_Text_3->setTextBackgroundColor(color);
            ui->textEdit_Text_3->textCursor();
        }
    }
}

void MainWindow::on_actionFont_of_Text_1_triggered()
{
    QFont current = ui->textEdit_Text_1->currentFont();
    bool bOk;
    QFont font = QFontDialog::getFont(&bOk, current);
    if (bOk) {
        ui->textEdit_Text_1->setCurrentFont(font);
    }
}

void MainWindow::on_actionFont_of_Text_2_triggered()
{
    QFont current = ui->textEdit_Text_2->currentFont();
    bool bOk;
    QFont font = QFontDialog::getFont(&bOk, current);
    if (bOk) {
        ui->textEdit_Text_2->setCurrentFont(font);
    }
}

void MainWindow::on_actionFont_of_Text_3_triggered()
{
    QFont current = ui->textEdit_Text_3->currentFont();
    bool bOk;
    QFont font = QFontDialog::getFont(&bOk, current);
    if (bOk) {
        ui->textEdit_Text_3->setCurrentFont(font);
    }
}

void MainWindow::on_actionColor_of_Text_1_triggered()
{
    QColor color = QColorDialog::getColor();
    if (color.isValid()) {
        ui->textEdit_Text_1->setTextColor(color);
    }
}

void MainWindow::on_actionColor_of_Text_2_triggered()
{
    QColor color = QColorDialog::getColor();
    if (color.isValid()) {
        ui->textEdit_Text_2->setTextColor(color);
    }
}

void MainWindow::on_actionColor_of_Text_3_triggered()
{
    QColor color = QColorDialog::getColor();
    if (color.isValid()) {
        ui->textEdit_Text_3->setTextColor(color);
    }
}

void MainWindow::on_actionHighlight_in_Text_1_triggered()
{
    QColor color = QColorDialog::getColor();
    if (color.isValid()) {
        ui->textEdit_Text_1->setTextBackgroundColor(color);
    }
}

void MainWindow::on_actionHighlight_in_Text_2_triggered()
{
    QColor color = QColorDialog::getColor();
    if (color.isValid()) {
        ui->textEdit_Text_2->setTextBackgroundColor(color);
    }
}

void MainWindow::on_actionHighlight_in_Text_3_triggered()
{
    QColor color = QColorDialog::getColor();
    if (color.isValid()) {
        ui->textEdit_Text_3->setTextBackgroundColor(color);
    }
}

void MainWindow::on_actionAbout_triggered()
{
    QString about_pro = "This is a program for editing texts \n\n";
    about_pro += "Copyright (C) 2022 Aleksandr Migunov \n\n";
    about_pro += "This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License ";
    about_pro += "as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. \n\n";
    about_pro += "This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of";
    about_pro += " MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. \n\n";
    about_pro += "You should have received a copy of the GNU General Public License along with this program. ";
    about_pro += "If not, see <https://www.gnu.org/licenses/>.";

    QMessageBox::about(this, "About Program", about_pro);
}

void MainWindow::on_actionAbout_Qt_triggered()
{
    QMessageBox::aboutQt(this);
}
