---
title: "Multi-Mission SAR: The Missing Piece"
date: 2025-06-01T00:00:00-05:00
draft: false
author: "Forrest Williams"
description: "Single mission SAR isn't good enough anymore"
toc: 
---
Working at the Alaska Satellite Facility, I get to see all kinds of people working with SAR data - scientists, emergency responders, government officials, and businesses, just to name a few. The diversity of users and use cases is incredible, and the pace of progress in the SAR industry has been just as impressive.

We now have decades of historical SAR records, open-access missions like Sentinel-1 that scan the globe every twelve days, and a growing fleet of commercial missions that can deliver half-meter resolution imagery from almost anywhere, often within a few hours. The algorithms for detecting floods, fires, landslides, building damage, and more have never been better.
But when it comes to delivering on SAR’s full promise, we’re still falling short. As Brianna Pagan wrote in her [gut-wrenching post](https://www.linkedin.com/pulse/when-our-community-burned-where-satellite-information-pagán-phd-8rxwf) about her experience during the Palisades Fire, the “anytime, anywhere” promise of SAR (and many other response tools) wasn’t fulfilled.

<figure style="text-align: center;">
  <img src="/brianna_pagan_post.png" width="50%" title="Brianna Pagan's Recent LinkedIn Post">
  <figcaption>Brianna Pagan's Recent LinkedIn Post.</figcaption>
</figure>

Yes, we had a deep historical archive of Sentinel-1 data, and commercial SAR companies contributed freely available imagery updated every few hours, but where was the mapping effort that pulled all this data together into a single, continuously updated damage map?

## What's wrong?
There are many reasons this didn’t happen, and we need to address them all, but I want to focus on one in particular: multi-mission data interoperability.
To detect damage, or any kind of change, state-of-the-art techniques need to compare the world before and after a disaster. Since we don’t know where disasters will happen ahead of time, we need global monitoring for the “before” images and rapid follow-up acquisitions for the “after”.

Joe Morrison explains well in his [blog post on satellite mission design](https://joemorrison.substack.com/p/a-simple-mental-model-for-understanding) that it’s practically impossible to meet both needs with a single mission. There are tradeoffs between latency, resolution, and coverage and you can’t optimize for all three. Public missions like Sentinel-1 prioritize coverage and latency, making them ideal for monitoring. Commercial missions prioritize latency and resolution, making them ideal for mobilization.

<figure style="text-align: center;">
  <img src="/sar_mission_venn.svg" width="75%" title="Joe Morrison's Satellite Mision Mental Model.">
  <figcaption>Joe Morrison's Satellite Mision Mental Model.</figcaption>
</figure>

But during a disaster, we need *both*. We need a multi-mission framework that lets us use each kind of data for what it does best. That means building a baseline archive from public missions, then rapidly tasking commercial satellites when disasters strike.

The frustrating part is we already have access to both types of data. But using them together is still extremely difficult. Geolocation is often unreliable (I’ve seen examples from every major commercial provider with errors of half a kilometer or more), pixel values don’t match across datasets, and viewing angles vary widely, affecting the return signal. I could go on, but you get the point.

## What we can do
Fortunately, these are solvable problems. Better geocoding and radiometric terrain correction (RTC) can address many of these issues and the datasets already include the metadata needed to perform these corrections. And this isn’t just theoretical. I’ve been working on a new Python package called [MultiRTC](https://github.com/forrestfwilliams/multirtc), which shows how the RTC workflow from the [OPERA](https://www.jpl.nasa.gov/go/opera/about-opera/) and [ISCE3](https://github.com/isce-framework/isce3) JPL teams can improve the geolocation and radiometric accuracy of both public and commercial SAR datasets.

It’s still early days, but I’m hopeful that this package can be extended to produce RTC products for every major public and commercial SAR dataset, easing some of the issues I’ve described.

So before we get too excited about new satellite capabilities, let’s ask ourselves: are we fully using what we already have? I don’t think the challenges Brianna highlighted will be solved by the next new mission. They’ll be solved, at least in part, by figuring out how to better combine the capabilities we already have.
