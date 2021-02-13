package com.konkuk.hoeunlee;

import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.filechooser.FileNameExtensionFilter;

@SuppressWarnings("serial")
public class MyFrame extends JFrame {

    private List<Word> voc2 = new ArrayList<>();

    /* STEP */
    private String STEP;

    /* FILE PATH */
    private String FILE_PATH;

    private String resultString;

    /* Container */
    Container frame = getContentPane();

    JPanel titleTextPanel;
    ImageIcon backIcon = new ImageIcon("img/back.png");
    JButton backButton;

    /* TITLE PAGE */
    JPanel titlePanel;
    JPanel namePanel;
    JButton button1;
    JButton button2;
    JButton button3;
    JButton button4;
    JButton button5;
    JButton changeFileButton;

    /* SEARCH PAGE */
    JTextField searchField;
    ButtonGroup group = new ButtonGroup();
    JRadioButton[] radioButton = new JRadioButton[3];
    private int searchType;
    JList<String> list;
    DefaultListModel<String> model;

    /* QUIZ PAGE */
    JPanel questionPanel;
    JLabel questionLabel;
    ButtonGroup answerGroup = new ButtonGroup();
    JRadioButton[] answerRadioButton = new JRadioButton[4];
    private int nowAnswer;
    private boolean answerFlag;
    JLabel background, process;
    JButton okButton;
    Thread quizThread;

    /* Practice */
    JTextField enterField;
    JPanel practicePanel;
    JLabel practiceLabel;
    JLabel pBackground, pProcess;
    private boolean enterFlag;
    Thread practiceThread;

    /* Frequent words */
    JList<String> fList;
    DefaultListModel<String> fModel;

    /* Edit */
    JTextField korField, engField;
    JPanel korPanel, engPanel;
    JList<String> eList;
    DefaultListModel<String> eModel;
    JButton addButton;
    private boolean deleteFlag;

    public MyFrame() {
        this("JAVA 과제5 - 202011353 이호은");
    }

    public MyFrame(String title) {
        super(title);
        this.setSize(800, 480);
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        TitleInit();
        STEP = "TITLE";
        FILE_PATH = "data/quiz.txt";
        makeVoc(FILE_PATH);
        this.setVisible(true);
    }

    /* Open Page with FLAG*/
    public void OpenScreen() {
        switch (STEP) {
            case "TITLE":
                TitleInit();
                break;

            case "SEARCH":
                searchType = 0;
                SearchInit();
                break;

            case "QUIZ":
                QuizInit();
                break;

            case "PRACTICE":
                Practice();
                break;

            case "HISTORY":
                HistoryInit();
                break;

            case "EDIT":
                EditInit();
                break;
        }
    }

    /* TITLE PAGE */
    public void TitleInit() {
        frame.setLayout(null);
        frame.setBackground(Color.WHITE);

        /* Title Panel */
        titlePanel = new JPanel();
        JLabel titleLabel = new JLabel();
        titleLabel.setText("My Voca!");
        titleLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 36));
        titlePanel.add(titleLabel);
        titlePanel.setBackground(Color.WHITE);
        titlePanel.setSize(300, 60);
        titlePanel.setLocation(250, 30);
        frame.add(titlePanel);

        /* Name Panel */
        namePanel = new JPanel();
        JLabel nameLabel = new JLabel();
        nameLabel.setText("JAVA프로그래밍 | 202011353 | 이호은");
        nameLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        namePanel.add(nameLabel);
        namePanel.setBackground(Color.WHITE);
        namePanel.setSize(500, 30);
        namePanel.setLocation(150, 140);
        frame.add(namePanel);

        /* Search Button */
        button1 = new JButton();
        JLabel temp1 = new JLabel();
        temp1.setText("단어 검색");
        temp1.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        button1.add(temp1);
        button1.setBackground(Color.LIGHT_GRAY);
        button1.setSize(300, 40);
        button1.setLocation(250, 180);
        frame.add(button1);

        /* Quiz1 Button */
        button2 = new JButton();
        JLabel temp2 = new JLabel();
        temp2.setText("객관식 퀴즈 (단어 뜻 맞추기)");
        temp2.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        button2.add(temp2);
        button2.setBackground(Color.LIGHT_GRAY);
        button2.setSize(300, 40);
        button2.setLocation(250, 230);
        frame.add(button2);

        /* Quiz2 Button */
        button3 = new JButton();
        JLabel temp3 = new JLabel();
        temp3.setText("서술형 퀴즈 (영단어 맞추기)");
        temp3.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        button3.add(temp3);
        button3.setBackground(Color.LIGHT_GRAY);
        button3.setSize(300, 40);
        button3.setLocation(250, 280);
        frame.add(button3);

        /* History Button */
        button4 = new JButton();
        JLabel temp4 = new JLabel();
        temp4.setText("빈출 단어");
        temp4.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        button4.add(temp4);
        button4.setBackground(Color.LIGHT_GRAY);
        button4.setSize(300, 40);
        button4.setLocation(250, 330);
        frame.add(button4);

        /* Edit Button */
        button5 = new JButton();
        JLabel temp5 = new JLabel();
        temp5.setText("단어장 편집");
        temp5.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        button5.add(temp5);
        button5.setBackground(Color.LIGHT_GRAY);
        button5.setSize(300, 40);
        button5.setLocation(250, 380);
        frame.add(button5);

        /* change file Button */
        changeFileButton = new JButton();
        changeFileButton.setIcon(new ImageIcon("img/file.png"));
        changeFileButton.setSize(40, 40);
        changeFileButton.setLocation(720, 380);
        frame.add(changeFileButton);

        /* add Action Listener */
        ActionListener titleActionListener = new TitleActionListener();
        button1.addActionListener(titleActionListener);
        button2.addActionListener(titleActionListener);
        button3.addActionListener(titleActionListener);
        button4.addActionListener(titleActionListener);
        button5.addActionListener(titleActionListener);

        /* file choosing action button */
        changeFileButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                /* File Dialog */
                JFileChooser chooser = new JFileChooser();
                chooser.setFileFilter(new FileNameExtensionFilter("text file (*.txt)", "txt"));
                int ret = chooser.showOpenDialog(null);
                if (ret != JFileChooser.APPROVE_OPTION) {
                    JOptionPane.showMessageDialog(null, "파일이 선택되지 않아 기본 파일이 선택됩니다.", "경고", JOptionPane.WARNING_MESSAGE);
                    FILE_PATH = "data/quiz.txt";
                } else {
                    String fileName = chooser.getSelectedFile().getName();
                    if (fileName.contains(".txt")) {
                        FILE_PATH = chooser.getSelectedFile().getPath();
                    } else {
                        JOptionPane.showMessageDialog(null, "txt 형식의 파일이 아닙니다. 기본 파일이 선택됩니다.", "경고", JOptionPane.WARNING_MESSAGE);
                    }
                }
                voc2.clear();
                makeVoc(FILE_PATH);
            }
        });

        this.setVisible(true);
    }

    /* SEARCH PAGE */
    public void SearchInit() {
        frame.setLayout(null);
        frame.setBackground(Color.WHITE);

        backButton = new JButton();
        backButton.setIcon(backIcon);
        backButton.setSize(24, 24);
        backButton.setLocation(10, 20);
        backButton.setBorder(null);
        frame.add(backButton);

        titleTextPanel = new JPanel();
        JLabel titleLabel = new JLabel();
        titleLabel.setText("단어 검색");
        titleLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 20));
        titleTextPanel.add(titleLabel);
        titleTextPanel.setBackground(Color.WHITE);
        titleTextPanel.setSize(80, 26);
        titleTextPanel.setLocation(32, 16);
        frame.add(titleTextPanel);

        searchField = new JTextField();
        searchField.setSize(400, 40);
        searchField.setFont(new Font("나눔스퀘어", Font.PLAIN, 18));
        searchField.setBackground(Color.WHITE);
        searchField.setLocation(200, 70);
        frame.add(searchField);

        RadioItemListener radioItemListener = new RadioItemListener();
        radioButton[0] = new JRadioButton("완전 일치");
        radioButton[0].setFont(new Font("나눔스퀘어", Font.PLAIN, 12));
        radioButton[1] = new JRadioButton("일부 일치");
        radioButton[1].setFont(new Font("나눔스퀘어", Font.PLAIN, 12));
        radioButton[2] = new JRadioButton("전체 보기");
        radioButton[2].setFont(new Font("나눔스퀘어", Font.PLAIN, 12));
        group.add(radioButton[0]);
        group.add(radioButton[1]);
        group.add(radioButton[2]);
        radioButton[0].addItemListener(radioItemListener);
        radioButton[1].addItemListener(radioItemListener);
        radioButton[2].addItemListener(radioItemListener);

        radioButton[0].setSize(100, 30);
        radioButton[0].setBackground(Color.WHITE);
        radioButton[0].setLocation(250, 120);
        frame.add(radioButton[0]);

        radioButton[1].setSize(100, 30);
        radioButton[1].setBackground(Color.WHITE);
        radioButton[1].setLocation(360, 120);
        frame.add(radioButton[1]);

        radioButton[2].setSize(100, 30);
        radioButton[2].setBackground(Color.WHITE);
        radioButton[2].setLocation(470, 120);
        frame.add(radioButton[2]);

        model = new DefaultListModel<>();
        list = new JList<>(model);
        list.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        JScrollPane scrollPane = new JScrollPane(list);
        scrollPane.setSize(400, 240);
        scrollPane.setBackground(Color.LIGHT_GRAY);
        scrollPane.setLocation(200, 160);
        frame.add(scrollPane);

        searchField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                model.clear();
                if (searchType == 0) {
                    JOptionPane.showMessageDialog(null, "검색 조건이 선택되지 않았습니다.", "경고", JOptionPane.WARNING_MESSAGE);
                }
                // 포함된 단어 검색
                else if (searchType == -1) {
                    resultString = searchVoc2(searchField.getText());
                }
                // 완벽 일치 단어 검색
                else if (searchType == 1) {
                    resultString = searchVoc(searchField.getText());
                }

                String[] temp = resultString.split("&");
                for (String str : temp) {
                    model.addElement(str);
                }
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                STEP = "TITLE";
                frame.removeAll();
                frame.repaint();
                OpenScreen();
            }
        });

        this.setVisible(true);
    }

    /* QUIZ PAGE */
    public void QuizInit() {
        frame.setLayout(null);
        frame.setBackground(Color.WHITE);

        backButton = new JButton();
        backButton.setIcon(backIcon);
        backButton.setSize(24, 24);
        backButton.setLocation(10, 20);
        backButton.setBorder(null);
        frame.add(backButton);

        titleTextPanel = new JPanel();
        JLabel titleLabel = new JLabel();
        titleLabel.setText("객관식 퀴즈");
        titleLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 20));
        titleTextPanel.add(titleLabel);
        titleTextPanel.setBackground(Color.WHITE);
        titleTextPanel.setSize(100, 26);
        titleTextPanel.setLocation(32, 16);
        frame.add(titleTextPanel);

        background = new JLabel();
        background.setOpaque(true);
        background.setBackground(Color.LIGHT_GRAY);
        background.setSize(400, 5);
        background.setLocation(200, 100);

        process = new JLabel();
        process.setOpaque(true);
        process.setBackground(Color.PINK);
        process.setSize(0, 5);
        process.setLocation(200, 100);

        questionPanel = new JPanel();
        questionLabel = new JLabel();
        questionLabel.setText("");
        questionLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 20));
        questionPanel.add(questionLabel);
        questionPanel.setBackground(Color.WHITE);
        questionPanel.setSize(500, 40);
        questionPanel.setLocation(150, 160);
        frame.add(questionPanel);

        frame.add(process);
        frame.add(background);

        okButton = new JButton();
        JLabel okLabel = new JLabel();
        okLabel.setText("OK");
        okLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        okButton.add(okLabel);
        okButton.setBackground(Color.LIGHT_GRAY);
        okButton.setSize(300, 40);
        okButton.setLocation(250, 370);
        okButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (nowAnswer == 1 || nowAnswer == 2 || nowAnswer == 3 || nowAnswer == 4) {
                    answerFlag = true;
                }
            }
        });
        frame.add(okButton);

        answerRadioButton[0] = new JRadioButton();
        answerRadioButton[0].setFont(new Font("나눔스퀘어", Font.PLAIN, 12));
        answerRadioButton[1] = new JRadioButton();
        answerRadioButton[1].setFont(new Font("나눔스퀘어", Font.PLAIN, 12));
        answerRadioButton[2] = new JRadioButton();
        answerRadioButton[2].setFont(new Font("나눔스퀘어", Font.PLAIN, 12));
        answerRadioButton[3] = new JRadioButton();
        answerRadioButton[3].setFont(new Font("나눔스퀘어", Font.PLAIN, 12));

        AnswerItemListener itemListener = new AnswerItemListener();
        for (JRadioButton b : answerRadioButton) {
            answerGroup.add(b);
            b.addItemListener(itemListener);
            b.setSize(200, 30);
            b.setBackground(Color.WHITE);
        }

        answerRadioButton[0].setLocation(300, 220);
        answerRadioButton[1].setLocation(300, 250);
        answerRadioButton[2].setLocation(300, 280);
        answerRadioButton[3].setLocation(300, 310);

        frame.add(answerRadioButton[0]);
        frame.add(answerRadioButton[1]);
        frame.add(answerRadioButton[2]);
        frame.add(answerRadioButton[3]);

        quizThread = new Thread() {
            @Override
            public void run() {
                multipleChoiceQuiz();
                super.interrupt();
            }
        };
        quizThread.start();

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                STEP = "TITLE";
                frame.removeAll();
                frame.repaint();
                OpenScreen();
                quizThread.interrupt();
            }
        });

        this.setVisible(true);
    }

    public void Practice() {
        enterFlag = false;

        frame.setLayout(null);
        frame.setBackground(Color.WHITE);

        enterField = new JTextField();
        enterField.setSize(400, 40);
        enterField.setFont(new Font("나눔스퀘어", Font.PLAIN, 18));
        enterField.setBackground(Color.WHITE);
        enterField.setLocation(200, 370);
        frame.add(enterField);

        backButton = new JButton();
        backButton.setIcon(backIcon);
        backButton.setSize(24, 24);
        backButton.setLocation(10, 20);
        backButton.setBorder(null);
        frame.add(backButton);

        titleTextPanel = new JPanel();
        JLabel titleLabel = new JLabel();
        titleLabel.setText("서술형 퀴즈");
        titleLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 20));
        titleTextPanel.add(titleLabel);
        titleTextPanel.setBackground(Color.WHITE);
        titleTextPanel.setSize(100, 26);
        titleTextPanel.setLocation(32, 16);
        frame.add(titleTextPanel);

        practicePanel = new JPanel();
        practiceLabel = new JLabel();
        practiceLabel.setText("1. ~");
        practiceLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 20));
        practicePanel.add(practiceLabel);
        practicePanel.setBackground(Color.WHITE);
        practicePanel.setSize(800, 40);
        practicePanel.setLocation(0, 160);
        frame.add(practicePanel);

        pBackground = new JLabel();
        pBackground.setOpaque(true);
        pBackground.setBackground(Color.LIGHT_GRAY);
        pBackground.setSize(400, 5);
        pBackground.setLocation(200, 100);

        pProcess = new JLabel();
        pProcess.setOpaque(true);
        pProcess.setBackground(Color.PINK);
        pProcess.setSize(0, 5);
        pProcess.setLocation(200, 100);

        frame.add(pProcess);
        frame.add(pBackground);

        enterField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!enterField.getText().equals("")) {
                    enterFlag = true;
                }
            }
        });

        practiceThread = new Thread() {
            @Override
            public void run() {
                practiceQuiz();
                super.interrupt();
            }
        };
        practiceThread.start();

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                STEP = "TITLE";
                frame.removeAll();
                frame.repaint();
                OpenScreen();
                practiceThread.interrupt();
            }
        });

        this.setVisible(true);
    }

    public void HistoryInit() {
        frame.setLayout(null);
        frame.setBackground(Color.WHITE);

        backButton = new JButton();
        backButton.setIcon(backIcon);
        backButton.setSize(24, 24);
        backButton.setLocation(10, 20);
        backButton.setBorder(null);
        frame.add(backButton);

        titleTextPanel = new JPanel();
        JLabel titleLabel = new JLabel();
        titleLabel.setText("빈출 단어");
        titleLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 20));
        titleTextPanel.add(titleLabel);
        titleTextPanel.setBackground(Color.WHITE);
        titleTextPanel.setSize(80, 26);
        titleTextPanel.setLocation(32, 16);
        frame.add(titleTextPanel);

        fModel = new DefaultListModel<>();
        fList = new JList<>(fModel);
        fList.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        JScrollPane scrollPane = new JScrollPane(fList);
        scrollPane.setSize(400, 340);
        scrollPane.setBackground(Color.LIGHT_GRAY);
        scrollPane.setLocation(200, 60);
        frame.add(scrollPane);

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                STEP = "TITLE";
                frame.removeAll();
                frame.repaint();
                OpenScreen();
            }
        });

        this.setVisible(true);

        FreqWord();
    }

    /* Edit Page */
    public void EditInit() {
        deleteFlag = false;
        frame.setLayout(null);
        frame.setBackground(Color.WHITE);

        backButton = new JButton();
        backButton.setIcon(backIcon);
        backButton.setSize(24, 24);
        backButton.setLocation(10, 20);
        backButton.setBorder(null);
        frame.add(backButton);

        titleTextPanel = new JPanel();
        JLabel titleLabel = new JLabel();
        titleLabel.setText("단어장 편집");
        titleLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 20));
        titleTextPanel.add(titleLabel);
        titleTextPanel.setBackground(Color.WHITE);
        titleTextPanel.setSize(110, 26);
        titleTextPanel.setLocation(32, 16);
        frame.add(titleTextPanel);

        engField = new JTextField();
        engField.setSize(180, 40);
        engField.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        engField.setBackground(Color.WHITE);
        engField.setLocation(178, 80);
        frame.add(engField);

        engPanel = new JPanel();
        JLabel engLabel = new JLabel();
        engLabel.setText("단어");
        engLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 14));
        engPanel.add(engLabel);
        engPanel.setBackground(Color.WHITE);
        engPanel.setSize(30, 20);
        engPanel.setLocation(142, 88);
        frame.add(engPanel);

        korField = new JTextField();
        korField.setSize(180, 40);
        korField.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        korField.setBackground(Color.WHITE);
        korField.setLocation(414, 80);
        frame.add(korField);

        korPanel = new JPanel();
        JLabel korLabel = new JLabel();
        korLabel.setText("의미");
        korLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 14));
        korPanel.add(korLabel);
        korPanel.setBackground(Color.WHITE);
        korPanel.setSize(30, 20);
        korPanel.setLocation(378, 88);
        frame.add(korPanel);

        addButton = new JButton();
        addButton.setIcon(new ImageIcon("img/add.png"));
        addButton.setBackground(Color.WHITE);
        addButton.setSize(40, 40);
        addButton.setLocation(614, 80);
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String eng = engField.getText().trim();
                String kor = korField.getText().trim();
                if (eng.length() > 0 && kor.length() > 0) {
                    int result = JOptionPane.showConfirmDialog(null, eng + " (" + kor + ") 을(를) 단어장에 추가하시겠습니까?", "확인", JOptionPane.YES_NO_OPTION);
                    if (result == JOptionPane.YES_OPTION) {
                        addWord(new Word(eng, kor));
                        update();
                    }
                    engField.setText("");
                    korField.setText("");
                } else {
                    JOptionPane.showMessageDialog(null, "단어와 뜻을 모두 입력해주세요.", "경고", JOptionPane.WARNING_MESSAGE);
                }
            }
        });
        frame.add(addButton);

        eModel = new DefaultListModel<>();
        eList = new JList<>(eModel);
        eList.setFont(new Font("나눔스퀘어", Font.PLAIN, 16));
        JScrollPane scrollPane = new JScrollPane(eList);
        scrollPane.setSize(400, 260);
        scrollPane.setBackground(Color.LIGHT_GRAY);
        scrollPane.setLocation(200, 170);
        frame.add(scrollPane);

        JPanel infoPanel = new JPanel();
        JLabel infoLabel = new JLabel();
        infoLabel.setText("* 단어를 클릭해서 삭제하세요.");
        infoLabel.setFont(new Font("나눔스퀘어", Font.PLAIN, 12));
        infoPanel.add(infoLabel);
        infoPanel.setBackground(Color.WHITE);
        infoPanel.setSize(400, 30);
        infoPanel.setLocation(200, 140);
        frame.add(infoPanel);

        update();

        eList.addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
                if (!deleteFlag) {
                    if (!e.getValueIsAdjusting()) {
                        String eng = eList.getSelectedValue();
                        int result = JOptionPane.showConfirmDialog(null, eng + "(을)를 삭제하시겠습니까?", "확인", JOptionPane.YES_NO_OPTION);
                        if (result == JOptionPane.YES_OPTION) {
                            deleteFlag = true;
                            deleteWord(eng);
                        }
                    }
                }

            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                STEP = "TITLE";
                frame.removeAll();
                frame.repaint();
                OpenScreen();
            }
        });

        this.setVisible(true);
    }

    public void update() {
        eModel.clear();
        resultString = showEngAll();
        String[] temp = resultString.split("&");
        for (String str : temp) {
            eModel.addElement(str);
        }
    }

    public class TitleActionListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            /* TITLE */
            if (e.getSource() == button1) {
                STEP = "SEARCH";
            } else if (e.getSource() == button2) {
                STEP = "QUIZ";
            } else if (e.getSource() == button3) {
                STEP = "PRACTICE";
            } else if (e.getSource() == button4) {
                STEP = "HISTORY";
            } else if (e.getSource() == button5) {
                STEP = "EDIT";
            }

            frame.removeAll();
            frame.repaint();
            OpenScreen();
        }

    }

    public class RadioItemListener implements ItemListener {

        @Override
        public void itemStateChanged(ItemEvent e) {
            model.clear();
            searchField.setText("");

            if (e.getSource() == radioButton[0]) {
                searchField.setEnabled(true);
                searchType = 1;
            } else if (e.getSource() == radioButton[1]) {
                searchField.setEnabled(true);
                searchType = -1;
            } else if (e.getSource() == radioButton[2]) {
                searchField.setEnabled(false);
                searchType = -2;
                resultString = showAll();
                String[] temp = resultString.split("&");
                for (String str : temp) {
                    model.addElement(str);
                }
            } else {
                searchType = 0;
            }
        }
    }

    public class AnswerItemListener implements ItemListener {

        @Override
        public void itemStateChanged(ItemEvent e) {
            if (e.getSource() == answerRadioButton[0]) {
                nowAnswer = 1;
                okButton.setEnabled(true);
            } else if (e.getSource() == answerRadioButton[1]) {
                nowAnswer = 2;
                okButton.setEnabled(true);
            } else if (e.getSource() == answerRadioButton[2]) {
                nowAnswer = 3;
                okButton.setEnabled(true);
            } else if (e.getSource() == answerRadioButton[3]) {
                nowAnswer = 4;
                okButton.setEnabled(true);
            } else {
                nowAnswer = 0;
            }
        }
    }

    void addWord(Word word) {
        voc2.add(word);
    }

    void deleteWord(String english) {
        for (int i = 0; i < voc2.size(); i++) {
            if (voc2.get(i).eng.equals(english)) {
                voc2.remove(i);
                break;
            }
        }

        eModel.clear();
        resultString = showEngAll();
        String[] temp = resultString.split("&");
        for (String str : temp) {
            eModel.addElement(str);
        }
        deleteFlag = false;
    }

    void makeVoc(String fileName) {
        try (Scanner s = new Scanner(new File(fileName), "UTF-8")) {
            while (s.hasNextLine()) {
                String str = s.nextLine();
                String[] temp = str.split("\t");
                this.addWord(new Word(temp[0].trim(), temp[1].trim()));
            }
        } catch (FileNotFoundException e) {
            JOptionPane.showMessageDialog(null, "파일을 찾을 수 없습니다.", "오류", JOptionPane.WARNING_MESSAGE);
        } finally {
            if (voc2.size() == 0) {
                JOptionPane.showMessageDialog(null, "단어장을 생성할 수 없습니다. 기본 파일로 변경합니다.", "파일 포맷 오류", JOptionPane.WARNING_MESSAGE);
                FILE_PATH = "data/quiz.txt";
                voc2.clear();
                makeVoc(FILE_PATH);
            }
        }
    }

    public String searchVoc(String keyword) {
        int count = 0;
        String result = "";

        // 아무것도 입력 안하고 검색 시도한 경우
        if (keyword.isEmpty()) {
            JOptionPane.showMessageDialog(null, "검색어를 입력하세요.", "경고", JOptionPane.WARNING_MESSAGE);
            return "";
        }

        keyword = keyword.trim();

        for (Word word : voc2) {
            if (word != null) {
                if (word.eng.equals(keyword)) {
                    result = result.concat("뜻 : " + word.kor);
                    count++;
                    break;
                }
            } else {
                break;
            }
        }

        // 검색어와 맞는 단어 없으면
        if (count == 0)
            JOptionPane.showMessageDialog(null, "단어가 없습니다.", "안내", JOptionPane.INFORMATION_MESSAGE);

        return result;
    }

    public String searchVoc2(String keyword) {
        int count = 0;
        String result = "";

        // 아무것도 입력 안하고 검색 시도한 경우
        if (keyword.isEmpty()) {
            JOptionPane.showMessageDialog(null, "검색어를 입력하세요.", "경고", JOptionPane.WARNING_MESSAGE);
            return "";
        }

        keyword = keyword.trim();

        for (Word word : voc2) {
            if (word != null) {
                if (word.eng.contains(keyword) || word.kor.contains(keyword)) {
                    result = result.concat((count + 1) + ") " + word.eng + " (" + word.kor + ")&");
                    count++;
                }
            } else {
                break;
            }
        }

        // 검색어와 맞는 단어 없으면
        if (count == 0)
            JOptionPane.showMessageDialog(null, "단어가 없습니다.", "안내", JOptionPane.INFORMATION_MESSAGE);

        return result;
    }

    public String showAll() {
        int count = 1;
        String result = "";
        for (Word word : voc2) {
            if (word != null) {
                result = result.concat(count++ + ") " + word.eng + " (" + word.kor + ")&");
            } else {
                break;
            }
        }
        return result;
    }

    public String showEngAll() {
        String result = "";
        for (Word word : voc2) {
            if (word != null) {
                result = result.concat(word.eng + "&");
            } else {
                break;
            }
        }
        return result;
    }

    public void FreqWord() {
        List<Word> list = new ArrayList<>(voc2);

        Collections.sort(list);

        if (list.get(0).count == 0) {
            fModel.addElement("아직 출제된 단어가 없습니다.");
        } else {
            for (Word w : list) {
                if (w.count != 0)
                    fModel.addElement(w.eng + " (" + w.kor + ") : " + w.count + "회");
            }
        }
    }

    public void multipleChoiceQuiz() {
        answerFlag = false;
        okButton.setEnabled(false);
        final int MAXV = 10;
        int right = 0;

        // 시작 시간 체크
        Calendar start = Calendar.getInstance();
        int startHour = start.get(Calendar.HOUR_OF_DAY);
        int startMinute = start.get(Calendar.MINUTE);
        int startSecond = start.get(Calendar.SECOND);

        Random random = new Random();
        List<String> check = new ArrayList<>();

        for (int i = 1; i <= MAXV; i++) {
            int wordToPrint = random.nextInt(voc2.size());

            Word nowWord = voc2.get(wordToPrint);
            voc2.get(wordToPrint).CountUp();
            questionLabel.setText(i + ". " + nowWord.eng + "의 뜻은 무엇인가요?");

            int numberOfAnswer = random.nextInt(4) + 1;
            int wrongToPrint;

            for (int j = 1; j <= 4; j++) {
                if (j == numberOfAnswer) {
                    answerRadioButton[j - 1].setText(j + ") " + nowWord.kor.trim());
                } else {
                    while (true) {
                        wrongToPrint = random.nextInt(voc2.size());

                        if (wrongToPrint != numberOfAnswer) {
                            if (check.contains(voc2.get(wrongToPrint).kor.trim())
                                    || nowWord.kor.trim().contains(voc2.get(wrongToPrint).kor.trim())
                                    || voc2.get(wrongToPrint).kor.trim().contains(nowWord.kor.trim())) {
                                continue;
                            }
                            check.add(voc2.get(wrongToPrint).kor.trim());
                            answerRadioButton[j - 1].setText(j + ") " + voc2.get(wrongToPrint).kor.trim());
                            break;
                        }
                    }
                }
            }

            process.setSize((int) (((double) i / (double) 10) * 400), 5);
            check.clear();

            while (!answerFlag) {
                try {
                    Thread.sleep(1);
                } catch (InterruptedException e) {
                    //e.printStackTrace();
                    return;
                }
            }
            answerFlag = false;

            if (nowAnswer == numberOfAnswer) {
                JOptionPane.showMessageDialog(null, "정답을 맞추셨습니다.", "정답입니다", JOptionPane.INFORMATION_MESSAGE);
                right++;
            } else {
                JOptionPane.showMessageDialog(null, "정답은 \"" + numberOfAnswer + ") " + nowWord.kor.trim() + "\" 입니다.",
                        "오답입니다.", JOptionPane.WARNING_MESSAGE);
            }
            nowAnswer = 0;

            answerGroup.clearSelection();

            okButton.setEnabled(false);
        }

        Calendar end = Calendar.getInstance();

        int endHour = end.get(Calendar.HOUR_OF_DAY);
        int endMinute = end.get(Calendar.MINUTE);
        int endSecond = end.get(Calendar.SECOND);

        int tHour = (endHour - startHour) * 3600;
        int tMin = (endMinute - startMinute) * 60;
        int tSec = endSecond - startSecond;
        int totalSec = (tHour + tMin + tSec) % 60;
        int totalMin = (tHour + tMin + tSec) / 60;

        if (totalMin != 0) {
            JOptionPane.showMessageDialog(null, totalMin + "분 " + totalSec + "초 소요되었습니다.",
                    MAXV + "개 중 " + right + "개 정답!", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(null, totalSec + "초 소요되었습니다.",
                    MAXV + "개 중 " + right + "개 정답!", JOptionPane.INFORMATION_MESSAGE);
        }

        questionLabel.setText("종료되었습니다.");
    }

    public void practiceQuiz() {
        enterFlag = false;
        final int MAXV = 10;
        int right = 0;

        // 시작 시간 체크
        Calendar start = Calendar.getInstance();
        int startHour = start.get(Calendar.HOUR_OF_DAY);
        int startMinute = start.get(Calendar.MINUTE);
        int startSecond = start.get(Calendar.SECOND);

        Random random = new Random();

        for (int i = 1; i <= MAXV; i++) {
            int wordToPrint = random.nextInt(voc2.size());

            Word nowWord = voc2.get(wordToPrint);
            voc2.get(wordToPrint).CountUp();
            practiceLabel.setText(i + ". \"" + nowWord.kor + "\"(이)라는 뜻을 가진 영어단어를 입력하세요.");

            pProcess.setSize((int) (((double) i / (double) 10) * 400), 5);

            while (!enterFlag) {
                try {
                    Thread.sleep(1);
                } catch (InterruptedException e) {
                    // e.printStackTrace();
                    return;
                }
            }
            enterFlag = false;

            String entered = enterField.getText();
            if (entered.equals(nowWord.eng)) {
                JOptionPane.showMessageDialog(null, "정답을 맞추셨습니다.", "정답입니다", JOptionPane.INFORMATION_MESSAGE);
                right++;
            } else {
                JOptionPane.showMessageDialog(null, "정답은 \"" + nowWord.eng + "\" 입니다.",
                        "오답입니다.", JOptionPane.WARNING_MESSAGE);
            }
            enterField.setText("");
            nowAnswer = 0;
        }

        Calendar end = Calendar.getInstance();

        int endHour = end.get(Calendar.HOUR_OF_DAY);
        int endMinute = end.get(Calendar.MINUTE);
        int endSecond = end.get(Calendar.SECOND);

        int tHour = (endHour - startHour) * 3600;
        int tMin = (endMinute - startMinute) * 60;
        int tSec = endSecond - startSecond;
        int totalSec = (tHour + tMin + tSec) % 60;
        int totalMin = (tHour + tMin + tSec) / 60;

        if (totalMin != 0) {
            JOptionPane.showMessageDialog(null, totalMin + "분 " + totalSec + "초 소요되었습니다.",
                    MAXV + "개 중 " + right + "개 정답!", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(null, totalSec + "초 소요되었습니다.",
                    MAXV + "개 중 " + right + "개 정답!", JOptionPane.INFORMATION_MESSAGE);
        }

        practiceLabel.setText("종료되었습니다.");
        enterField.setEnabled(false);
    }
}
