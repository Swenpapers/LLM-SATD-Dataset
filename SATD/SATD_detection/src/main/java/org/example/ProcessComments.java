package org.example;
import satd_detector.core.utils.SATDDetector;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class ProcessComments {
    public static void main(String[] args) {
        String inputFile = "/Users/ahmedaljohani/Apps/SATD_Transfomer/GetPyFiles/Json_File_info/Cleaned_Comments.csv";
        String outputFile = "satd_comments.csv";
        try (
                Scanner scanner = new Scanner(new FileInputStream(inputFile), StandardCharsets.UTF_8);
                PrintWriter writer = new PrintWriter(new OutputStreamWriter(new FileOutputStream(outputFile), StandardCharsets.UTF_8));
        ) {
            SATDDetector detector = new SATDDetector(); // Using built-in models
            if (scanner.hasNextLine()) {
                // Write headers as they are in the input file
                String header = scanner.nextLine();
                writer.println(header); // Print the header line to the output
            }

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] data = line.split(",", -1); // Better handling of empty fields
                if (data.length >= 3) {
                    String comment = data[2];
                    if (detector.isSATD(comment)) {
                        writer.println(line); // Write the entire line to output
                    }
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
