15 of the most common tradeoffs in System Design:

1. 𝐒𝐜𝐚𝐥𝐚𝐛𝐢𝐥𝐢𝐭𝐲 𝐯𝐬. 𝐏𝐞𝐫𝐟𝐨𝐫𝐦𝐚𝐧𝐜𝐞: Grow the system to handle more work vs. execute tasks faster.

2. 𝐕𝐞𝐫𝐭𝐢𝐜𝐚𝐥 𝐯𝐬. 𝐇𝐨𝐫𝐢𝐳𝐨𝐧𝐭𝐚𝐥 𝐒𝐜𝐚𝐥𝐢𝐧𝐠: Scale up with more powerful hardware vs. scale out by adding more servers.

3. 𝐋𝐚𝐭𝐞𝐧𝐜𝐲 𝐯𝐬. 𝐓𝐡𝐫𝐨𝐮𝐠𝐡𝐩𝐮𝐭: Prioritize fast responses for individual tasks vs. maximize the number of tasks over time.

4. 𝐒𝐐𝐋 𝐯𝐬 𝐍𝐨𝐒𝐐𝐋 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞𝐬: Opt for structured data and strict schemas vs. embrace flexibility and scalability for varied data types.

5. 𝐂𝐨𝐧𝐬𝐢𝐬𝐭𝐞𝐧𝐜𝐲 𝐯𝐬. 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐢𝐥𝐢𝐭𝐲 (𝐂𝐀𝐏 𝐓𝐡𝐞𝐨𝐫𝐞𝐦): Guarantee up-to-date data everywhere vs. ensure system is always up.

6. 𝐒𝐭𝐫𝐨𝐧𝐠 𝐯𝐬 𝐄𝐯𝐞𝐧𝐭𝐮𝐚𝐥 𝐂𝐨𝐧𝐬𝐢𝐬𝐭𝐞𝐧𝐜𝐲: Need immediate data accuracy across all nodes vs. is a short delay acceptable for system availability?

7. 𝐑𝐞𝐚𝐝-𝐓𝐡𝐫𝐨𝐮𝐠𝐡 𝐯𝐬 𝐖𝐫𝐢𝐭𝐞-𝐓𝐡𝐫𝐨𝐮𝐠𝐡 𝐂𝐚𝐜𝐡𝐞: Fetch and cache data upon request, or write data to cache and database simultaneously for consistency.

8. 𝐒𝐲𝐧𝐜𝐡𝐫𝐨𝐧𝐨𝐮𝐬 𝐯𝐬. 𝐀𝐬𝐲𝐧𝐜𝐡𝐫𝐨𝐧𝐨𝐮𝐬 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠: Wait for each task to complete vs. move on and handle tasks as they finish.

9. 𝐁𝐚𝐭𝐜𝐡 𝐯𝐬 𝐒𝐭𝐫𝐞𝐚𝐦 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠: Process data in chunks vs. handle it in real-time as it arrives.

10. 𝐒𝐭𝐚𝐭𝐞𝐟𝐮𝐥 𝐯𝐬 𝐒𝐭𝐚𝐭𝐞𝐥𝐞𝐬𝐬 𝐀𝐫𝐜𝐡𝐢𝐭𝐞𝐜𝐭𝐮𝐫𝐞: Remember user sessions and data vs. treat each request as independent.

11. 𝐋𝐨𝐧𝐠 𝐏𝐨𝐥𝐥𝐢𝐧𝐠 𝐯𝐬 𝐖𝐞𝐛𝐒𝐨𝐜𝐤𝐞𝐭𝐬: Request waits for data vs. continuous two-way connection.

12. 𝐍𝐨𝐫𝐦𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧 𝐯𝐬. 𝐃𝐞𝐧𝐨𝐫𝐦𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧: Organize data to eliminate duplication vs. combine for faster reads at the cost of some redundancy.

13. 𝐌𝐨𝐧𝐨𝐥𝐢𝐭𝐡𝐢𝐜 𝐯𝐬. 𝐌𝐢𝐜𝐫𝐨𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬 𝐀𝐫𝐜𝐡𝐢𝐭𝐞𝐜𝐭𝐮𝐫𝐞: Build a single, unified application vs. develop a collection of independent, smaller services.

14. 𝐓𝐂𝐏 𝐯𝐬. 𝐔𝐃𝐏: Guarantee reliable and ordered data delivery vs. opt for faster, though potentially unordered, transmission.

15. 𝐑𝐄𝐒𝐓 𝐯𝐬. 𝐆𝐫𝐚𝐩𝐡𝐐𝐋: Use standard HTTP methods for data exchange vs. query precisely what you need from a single endpoint.
