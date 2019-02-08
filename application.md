Name/Vorname/Telefon/mailadresse/GitHub: logo
Team: nein

Bisherige OS-Projekte:

 - postix (ehemals c6sh): Kassensoftware für 33C3/MRMCD etc: https://github.com/c3cashdesk/postix
 - pretix: Mitarbeit am Presale-System für 33C3/MRMCD etc: http://github.com/pretix/pretix
 - django: Contributions zu Django und umliegenden Projekten (django-channels)

Projekttitel (70Z)
bumf - Budgets und moderne Finanzplanung

Welches Problem willst du mit deinem Projekt lösen? (700Z)

TODO: verweise/links
Private Finanzplanung macht das Leben leichter - gerade wenn man nicht viel Geld hat, ist es
umso wichtiger, zu wissen, wohin es wandert. Traditionelle Buchhaltungstools sind auf
Unternehmen ausgerichtet und entsprechend unschön zu bedienen, das macht niemand.
Über die letzten Jahre hat sich youneedabudget.com als Martkführer in Sachen bedienbarer,
menschenfreundlicher Finanzplanung gezeigt. YNAB ist aber closed-source und hosted in den USA,
unterstützt Konto-Integration nur für USA-Konten und wer will schon seine Finanzdaten
Leuten irgendwo im Netz geben?


Wie wird Dein Projekt dieses Problem lösen? (1300Z)

Ich werde große Teile von YNAB nachbauen, aber einiges dabei verbessern, und natürlich den
Quelltext auf GitHub zugänglich machen und mit einer leicht zu folgenden Installier-Anleitung
versehen. Parallel werde ich auch eine einfache Android-App zum Eintragen von Zahlungen unterwegs
hinzufügen.

Durch das Selber-Hosten entfällt der Ärger mit sehr sensiblen Daten auf anderer Leute Server.
(Da das System mehrere Nutzer unterstützt, kann man das auch in Gruppen hosten, etwa wie
Jabber-Server. Ich werde aus Datenschutz-Komplikationsgründen aber auf keinen Fall öffentliches
oder kommerzielles Hosting anbieten wollen.)
Durch den Einbau von FinTS/HBCI (seit ein paar Monaten gibt es da Bibliotheken für) wird der
Tracking-Prozess noch reibungsloser und motivert dadurch mehr dazu, auch am Ball zu bleiben.

Eine Liste der weniger relevanten geplanten Verbesserungen gegenüber YNAB steht im README im
Repo auf GitHub.


Themenschwerpunkt: Civic Tech
Themenschwerpunkt zweite Runde? Jupp

Wer ist die Zielgruppe? Wie profitiert sie vom Projekt? (700Z)

Zielgruppe sind besonders Leute, die mit ihrem Geld haushalten müssen. Natürlich kann jeder
von Übersicht über seine oder ihre Finanzen profitieren, aber besonders wichtig ist es doch,
wenn man nicht viel hat, und mit dem, was bleibt, so gut wie möglich auskommen möchte.
Durch regelmäßiges Notieren der Ausgabequellen sieht man schnell, wo man einsparen kann, und
ist auch motiviert, sich zu überlegen, wie man sein Geld aufteilen möchte. YNAB selber hat
einen ganz guten Überblick darüber, wieso und wie budgetieren hilft.

Hast Du schon an der Idee gearbeitet? Wenn ja, beschreibe kurz den aktuellen Stand und erkläre die Neuerung. (700Z)

Ich habe schon mit der Ausarbeitung angefangen. Es gibt ein ziemlich fertig implementiertes Datenmodell,
das etwa dem von YNAB entspricht, aber auch doppelte Buchführung zulässt, sollte man bumf später
für den Gebrauch von Freiberuflern ausbauen wollen. Das Frontend ist sehr rudimentär angefangen - 
man kann bereits Kontostände und Transaktionen sehen, aber noch keine Transaktionen eintragen; und die
Budget-Ansicht ist noch nicht angefangen.
Die nächsten Schritte wären, Budgets im Frontend abzubilden, editierbar zu machen und dann zu
weiteren Features wie Sparzielen, dem Speichern von Belegfotos/-scans und dem Entwickeln der App überzugehen.

Wie viele Stunden pro Woche wirst/werdet Du/Ihr in den 6 Monaten Förderzeitraum im Durchschnitt an der Umsetzung arbeiten?

8

Skizziere kurz die wichtigsten Meilensteine, die Du/Ihr im Förderzeitraum umsetzen willst/wollt. (700Z)

 - Fertigstellung der wichtigsten Features im Frontend
   - Budgets editieren
   - Transaktionen eintragen
   - Berichte/Auswertungen sehen
   - Sparziele abbilden
 - Entwickeln einer simplen App, um Zahlungen von unterwegs einzutragen
 - Dokumentation
   - API-Dokumentierung abschließen (bereits interaktiv und verfügbar)
   - Installation dokumentieren
   - Entwickler-Doku publizireen

Wenn meine Projektidee nicht gefördert wird, darf sie trotzdem auf prototypefund.de und in wissenschaftlichen Publikationen rund um das Programm veröffentlicht werden?
Jupp


